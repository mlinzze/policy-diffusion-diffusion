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

SENSITIVITY = False

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
## extrapolate solar_capacity into the future

SHIFT_DELTA = 5
ifile = 'total_electricity_solar_capacity_by_source.csv'
df_solar = pd.read_csv(os.path.join(DATAPATH, ifile))

## ================

states = df_solar['stateabbr'].unique()
df_states = pd.read_csv('./data/states.csv')
names2abbrv = dict(zip(df_states['state'].values, df_states['stateabbr'].values))

df_effectiveness = pd.read_csv('./data/solar_emission_savings.csv', sep=';', skiprows=5) # file from Gregor
df_effectiveness = df_effectiveness.iloc[:-4, :].rename(columns={'metric tons/MW': 'effectiveness_capacity'})
df_effectiveness['State'] = df_effectiveness['State'].apply(lambda x: x.split('(')[0].strip())
df_effectiveness['stateabbr'] = df_effectiveness['State'].apply(lambda x: names2abbrv.get(x, x))
df_effectiveness = df_effectiveness.loc[df_effectiveness['stateabbr'] != 'District Of Columbia', :]
df_effectiveness['effectiveness_capacity'] = df_effectiveness['effectiveness_capacity'].apply(lambda x: x.replace(',', '')).astype(float)
df_effectiveness = df_effectiveness.loc[:, ['stateabbr', 'effectiveness_capacity']]

## ================

df_solar = df_solar.merge(df_effectiveness, on=['stateabbr'], how='left')

df_solar['solar_capacity'] = df_solar['solar_capacity'].astype(float)
df_solar['solar_capacity_share'] = df_solar['solar_capacity'] / df_solar['total_capacity']
df_solar['year'] = df_solar['year'].astype(int)

df_solar = df_solar.sort_values(by=['stateabbr', 'year'], ascending=True, ignore_index=True)
df_solar['growth_trend'] = (df_solar['solar_capacity_share'] - df_solar.groupby('stateabbr')['solar_capacity_share'].shift(SHIFT_DELTA))/SHIFT_DELTA
df_solar['growth_trend'] = df_solar['growth_trend'].fillna(0.)

df_solar = df_solar.loc[df_solar['year'] == df_solar['year'].max(), :]
df_solar['year'] = FIRSTYEAR
df_solar = expand_df(df_solar, dims=['stateabbr', 'year'], values=[states, range(FIRSTYEAR, LASTYEAR+1, 1)])

## constant solar_capacity
df_solar['growth_constant'] = 0.
df_solar['solar_capacity_share_constant'] = df_solar.groupby('stateabbr')['solar_capacity_share'].ffill()

## solar_capacity extrapolated based on past trends
state2baseline = df_solar.groupby('stateabbr')['solar_capacity_share'].first()
df_solar['growth_trend'] = df_solar.groupby('stateabbr')['growth_trend'].ffill()
df_solar['growth_trend_cumulative'] = df_solar.groupby('stateabbr')['growth_trend'].transform(lambda x: x.cumsum())
df_solar['solar_capacity_share_trend'] = df_solar.apply(lambda x: state2baseline[x['stateabbr']] + x['growth_trend_cumulative'], axis=1)

df_solar['total_capacity'] = df_solar.groupby('stateabbr')['total_capacity'].ffill()
df_solar['effectiveness_capacity'] = df_solar.groupby('stateabbr')['effectiveness_capacity'].ffill()

df_solar = df_solar.drop(columns=['solar_capacity_share', 'growth_trend_cumulative'])

df_solar.to_csv(os.path.join(RESULTPATH, 'solar_capacity_scenarios.csv'), index=False)

## ============================

I = 5 # baseline probability = 0.05
J = 9 # diffusion coefficient = empirical

EFFECT_SIZE = 0.0288 / 100.

for scenario in ['constant', 'trend']:

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

	df_capacity = df.copy()
	df_emissions = df.copy()

	## ============================

	growth = 'growth_' + scenario
	solar_capacity = 'solar_capacity_share_' + scenario

	df_solar = pd.read_csv(os.path.join(RESULTPATH, 'solar_capacity_scenarios.csv'))
	df_solar = df_solar.sort_values(by=['stateabbr', 'year'], ascending=True).reset_index(drop=True)
	df_solar = df_solar.set_index(['stateabbr', 'year'])

	df_solar['growth_treated'] = df_solar[growth] + EFFECT_SIZE

	# loop over possible years of policy adoption
	for year in range(FIRSTYEAR, LASTYEAR, 1):

		print(year)
		index = df_solar.index.get_level_values('year') == year
		df_solar['solar_capacity_share_baseline'] = np.nan
		df_solar.loc[index, 'solar_capacity_share_baseline'] = df_solar.loc[index, solar_capacity]
		df_solar['solar_capacity_share_baseline'] = df_solar.groupby('stateabbr')['solar_capacity_share_baseline'].ffill()
		df_solar.loc[index, 'growth_treated_cumulative'] = 0.

		index = df_solar.index.get_level_values('year') > year
		df_solar.loc[index, 'growth_treated_cumulative'] = df_solar.loc[index, :].groupby('stateabbr')['growth_treated'].transform(lambda x: x.cumsum())
		df_solar['solar_capacity_share_treated'] = df_solar['solar_capacity_share_baseline'] + df_solar['growth_treated_cumulative']

		## =======

		df_solar['solar_capacity_share_baseline'] = df_solar['solar_capacity_share_baseline'].apply(lambda x: np.min([x, 1.]))
		df_solar['solar_capacity_share_treated'] = df_solar['solar_capacity_share_treated'].apply(lambda x: np.min([x, 1.]))

		df_solar['solar_capacity_total_baseline'] = df_solar['solar_capacity_share_baseline'] * df_solar['total_capacity']
		df_solar['solar_capacity_total_treated'] = df_solar['solar_capacity_share_treated'] * df_solar['total_capacity']

		additional_capacity = df_solar.groupby('stateabbr')['solar_capacity_total_treated'].last() - df_solar.groupby('stateabbr')['solar_capacity_total_baseline'].last()

		## =======

		df_solar['emissions_reduced_baseline'] = df_solar['solar_capacity_total_baseline'] * df_solar['effectiveness_capacity']
		df_solar['emissions_reduced_treated'] = df_solar['solar_capacity_total_treated'] * df_solar['effectiveness_capacity']
		reduced_emissions = df_solar.loc[index, :].groupby('stateabbr')['emissions_reduced_treated'].sum() - df_solar.loc[index, :].groupby('stateabbr')['emissions_reduced_baseline'].sum()

		index = df_capacity.index.get_level_values('year') == year
		df_capacity.loc[index, :] = df_capacity.loc[index, :].multiply(additional_capacity.values, axis='index')

		index = df_emissions.index.get_level_values('year') == year
		df_emissions.loc[index, :] = df_emissions.loc[index, :].multiply(reduced_emissions.values, axis='index')

	df_results = pd.DataFrame({'stateabbr': states})
	df_results = df_results.set_index('stateabbr')

	for stateabbr in states:

		df_results.loc[stateabbr, 'capacity_direct'] = df_capacity.loc[df_capacity.index.get_level_values('stateabbr') == stateabbr, stateabbr].sum(axis=0)
		df_results.loc[stateabbr, 'capacity_indirect'] = df_capacity.loc[df_capacity.index.get_level_values('stateabbr') != stateabbr, stateabbr].sum(axis=0) -\
											df_capacity.loc[df_capacity.index.get_level_values('stateabbr') != stateabbr, 'control'].sum(axis=0)


		df_results.loc[stateabbr, 'emissions_direct'] = df_emissions.loc[df_emissions.index.get_level_values('stateabbr') == stateabbr, stateabbr].sum(axis=0)
		df_results.loc[stateabbr, 'emissions_indirect'] = df_emissions.loc[df_emissions.index.get_level_values('stateabbr') != stateabbr, stateabbr].sum(axis=0) -\
											df_emissions.loc[df_emissions.index.get_level_values('stateabbr') != stateabbr, 'control'].sum(axis=0)

	df_results.to_csv(os.path.join(results_path, 'solar_expansion_{0:s}_{1:s}.csv'.format(scenario, METRIC)))
	# emissions are in t; solar capacity is in MW
