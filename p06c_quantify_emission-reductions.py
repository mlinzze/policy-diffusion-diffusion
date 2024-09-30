#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import copy
import itertools

import numpy as np
import pandas as pd


## ============================================================

from parameters import *

## ========================================================================================================== ##

FIRSTYEAR = 2024
LASTYEAR = 2050

METRIC = 'slpm'

SIMULATIONS_PATH = './simulations/'
EXPERIMENT = 'results_{0:s}_linear_future_2050_none'.format(METRIC)

## ============================

def expand_df(df, dims, values):
	df = df.set_index(dims)
	multi_index = (pd.MultiIndex.from_product(
			iterables=values,
			names=dims))
	df = df.reindex(multi_index, fill_value=np.nan).reset_index()
	df = df.sort_values(by=dims, ascending=True).reset_index(drop=True)
	return df

## ========================================================
## extrapolate emissions into the future

SHIFT_DELTA = 5

df_ghg = pd.read_csv(os.path.join(DATAPATH, 'ghg_emissions.csv'), sep=';') # in 1.e6 t = Mt
df_ghg = df_ghg.loc[:, ['State'] + [str(y) for y in range(1970, 2021+1, 1)]]
df_ghg = df_ghg.melt(id_vars=['State']).rename(columns={'variable': 'year', 'value': 'emissions'})
df_ghg = df_ghg.loc[~df_ghg['State'].isin(['Total of states', 'District of Columbia']), :]

df_states = pd.read_csv(os.path.join(DATAPATH, 'states.csv'))
names2abbrv = dict(zip(df_states['state'].values, df_states['stateabbr'].values))
df_ghg['stateabbr'] = df_ghg['State'].apply(lambda x: names2abbrv.get(x, x))

df_ghg = df_ghg.loc[:, ['stateabbr', 'year', 'emissions']] # in million metric tons
states = df_ghg['stateabbr'].unique()

df_ghg['emissions'] = df_ghg['emissions'].astype(float)
df_ghg['year'] = df_ghg['year'].astype(int)

df_ghg = df_ghg.sort_values(by=['stateabbr', 'year'], ascending=True, ignore_index=True)
df_ghg['growth_trend'] = (df_ghg['emissions']/df_ghg.groupby('stateabbr')['emissions'].shift(SHIFT_DELTA))**(1/ SHIFT_DELTA)

df_ghg = df_ghg.loc[df_ghg['year'] == df_ghg['year'].max(), :]
df_ghg['year'] = FIRSTYEAR
df_ghg = expand_df(df_ghg, dims=['stateabbr', 'year'], values=[states, range(FIRSTYEAR, LASTYEAR+1, 1)])

## constant emissions
df_ghg['growth_constant'] = 1.
df_ghg['emissions_constant'] = df_ghg.groupby('stateabbr')['emissions'].ffill()

## emissions extrapolated based on past trends
state2baseline = df_ghg.groupby('stateabbr')['emissions'].first()
df_ghg['growth_trend'] = df_ghg.groupby('stateabbr')['growth_trend'].ffill()

df_ghg['growth_trend_cumulative'] = df_ghg.groupby('stateabbr')['growth_trend'].transform(lambda x: x.cumprod())
df_ghg['emissions_trend'] = df_ghg.apply(lambda x: state2baseline[x['stateabbr']] * x['growth_trend_cumulative'], axis=1)

df_ghg = df_ghg.drop(columns=['emissions', 'growth_trend_cumulative'])

df_ghg.to_csv(os.path.join(RESULTPATH, 'emission_scenarios.csv'), index=False)

## ============================

I = 5 # baseline probability = 0.05
J = 9 # diffusion coefficient = empirical

EFFECT_SIZE = 0.01

for emission_scenario in ['constant', 'trend']:

	## ============================

	results_path = os.path.join(SIMULATIONS_PATH, EXPERIMENT)

	df = pd.read_csv(os.path.join(results_path, 'result_{0:s}_{1:d}_{2:d}_{3:d}.csv'.format('ANY', 0, I, J)), names=['year', 'stateabbr', 'control'])

	for stateabbr in states:

		df1 = pd.read_csv(os.path.join(results_path, 'result_{0:s}_{1:d}_{2:d}_{3:d}.csv'.format(stateabbr, 1, I, J)), names=['year', 'stateabbr', stateabbr])
		df = df.merge(df1, on=['stateabbr', 'year'])

	df = df.loc[df['stateabbr'].isin(states), :]
	df = df.loc[df['year'].between(FIRSTYEAR, LASTYEAR), :]
	df = df.sort_values(by=['stateabbr', 'year'], ascending=True).reset_index(drop=True)
	df = df.set_index(['stateabbr', 'year'])

	## ============================

	growth = 'growth_' + emission_scenario
	emissions = 'emissions_' + emission_scenario

	df_ghg = pd.read_csv(os.path.join(RESULTPATH, 'emission_scenarios.csv'))
	df_ghg = df_ghg.sort_values(by=['stateabbr', 'year'], ascending=True).reset_index(drop=True)
	df_ghg = df_ghg.set_index(['stateabbr', 'year'])

	df_ghg['growth_treated'] = df_ghg[growth] - EFFECT_SIZE

	for year in range(FIRSTYEAR, LASTYEAR, 1):

		print(year)
		index = df_ghg.index.get_level_values('year') == year
		df_ghg['emissions_baseline'] = np.nan
		df_ghg.loc[index, 'emissions_baseline'] = df_ghg.loc[index, emissions]
		df_ghg['emissions_baseline'] = df_ghg.groupby('stateabbr')['emissions_baseline'].ffill()
		df_ghg.loc[index, 'growth_treated_cumulative'] = 1.

		index = df_ghg.index.get_level_values('year') > year
		df_ghg.loc[index, 'growth_treated_cumulative'] = df_ghg.loc[index, :].groupby('stateabbr')['growth_treated'].transform(lambda x: x.cumprod())
		df_ghg['emissions_treated'] = df_ghg['emissions_baseline'] * df_ghg['growth_treated_cumulative']

		reductions = df_ghg.loc[index, :].groupby('stateabbr')[emissions].sum() - df_ghg.loc[index, :].groupby('stateabbr')['emissions_treated'].sum()

		index = df.index.get_level_values('year') == year
		df.loc[index, :] = df.loc[index, :].multiply(reductions.values, axis='index')

	df_results = pd.DataFrame({'stateabbr': states})
	df_results = df_results.set_index('stateabbr')

	for stateabbr in states:

		df_results.loc[stateabbr, 'direct'] = df.loc[df.index.get_level_values('stateabbr') == stateabbr, stateabbr].sum(axis=0)
		df_results.loc[stateabbr, 'indirect'] = df.loc[df.index.get_level_values('stateabbr') != stateabbr, stateabbr].sum(axis=0) -\
											df.loc[df.index.get_level_values('stateabbr') != stateabbr, 'control'].sum(axis=0)

	df_results.to_csv(os.path.join(results_path, 'emission_reductions_{0:s}_{1:s}.csv'.format(emission_scenario, METRIC)))
