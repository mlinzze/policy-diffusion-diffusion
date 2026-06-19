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

## main simulations with existing policies
POLICIES_MAIN = ['0', '1', '3', '5', '10', '20', '30']

## sensitivity simulations with no existing policies
POLICIES_SENSITIVITY = ['none']
I_SENSITIVITY = list(range(1, 10+1, 1))
J_SENSITIVITY = list(range(0, 5+1, 1)) + [9]

EFFECT_SIZE = 0.01

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
df_ghg['growth_trend'] = (df_ghg['emissions']/df_ghg.groupby('stateabbr')['emissions'].shift(SHIFT_DELTA))**(1/SHIFT_DELTA)

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
## define simulation tasks

simulation_tasks = []

for POLICIES in POLICIES_MAIN:
	simulation_tasks.append({
		'POLICIES': POLICIES,
		'I': 5,
		'J': 9
	})

for POLICIES in POLICIES_SENSITIVITY:
	for I in I_SENSITIVITY:
		for J in J_SENSITIVITY:
			simulation_tasks.append({
				'POLICIES': POLICIES,
				'I': I,
				'J': J
			})

## ============================

for task in simulation_tasks:

	POLICIES = task['POLICIES']
	I = task['I']
	J = task['J']

	EXPERIMENT = 'results_{0:s}_linear_future_2050_{1:s}'.format(METRIC, POLICIES)
	results_path = os.path.join(SIMULATIONS_PATH, EXPERIMENT)

	if not os.path.exists(results_path):
		print('Path does not exist:', results_path)
		continue

	for emission_scenario in ['constant', 'trend']:

		growth = 'growth_' + emission_scenario
		emissions = 'emissions_' + emission_scenario

		df_ghg = pd.read_csv(os.path.join(RESULTPATH, 'emission_scenarios.csv'))
		df_ghg = df_ghg.sort_values(by=['stateabbr', 'year'], ascending=True).reset_index(drop=True)
		df_ghg = df_ghg.set_index(['stateabbr', 'year'])

		df_ghg['growth_treated'] = df_ghg[growth] - EFFECT_SIZE

		reduction_rows = []

		for year in range(FIRSTYEAR, LASTYEAR, 1):

			print(POLICIES, I, J, emission_scenario, year)

			df_tmp = df_ghg.copy()

			index_year = df_tmp.index.get_level_values('year') == year
			df_tmp['emissions_baseline'] = np.nan
			df_tmp.loc[index_year, 'emissions_baseline'] = df_tmp.loc[index_year, emissions]
			df_tmp['emissions_baseline'] = df_tmp.groupby('stateabbr')['emissions_baseline'].ffill()

			df_tmp['growth_treated_cumulative'] = np.nan
			df_tmp.loc[index_year, 'growth_treated_cumulative'] = 1.

			index_future = df_tmp.index.get_level_values('year') > year
			df_tmp.loc[index_future, 'growth_treated_cumulative'] = (
				df_tmp.loc[index_future, :]
				.groupby('stateabbr')['growth_treated']
				.transform(lambda x: x.cumprod())
			)

			df_tmp['emissions_treated'] = (
				df_tmp['emissions_baseline']
				* df_tmp['growth_treated_cumulative']
			)

			reductions = (
				df_tmp.loc[index_future, :]
				.groupby('stateabbr')[emissions].sum()
				- df_tmp.loc[index_future, :]
				.groupby('stateabbr')['emissions_treated'].sum()
			)

			df_reductions_year = reductions.reset_index()
			df_reductions_year.columns = ['stateabbr', 'reduction']
			df_reductions_year['year'] = year
			reduction_rows.append(df_reductions_year)

		df_reductions = pd.concat(reduction_rows, ignore_index=True)

		df_results = pd.DataFrame({'stateabbr': states})
		df_results = df_results.set_index('stateabbr')

		for stateabbr in states:

			filename_treat = os.path.join(
				results_path,
				'result_{0:s}_{1:d}_{2:d}_{3:d}.csv'.format(stateabbr, 1, I, J)
			)

			if POLICIES == 'none':
				filename_control = os.path.join(
					results_path,
					'result_{0:s}_{1:d}_{2:d}_{3:d}.csv'.format('ANY', 0, I, J)
				)
			else:
				filename_control = os.path.join(
					results_path,
					'result_{0:s}_{1:d}_{2:d}_{3:d}.csv'.format(stateabbr, 0, I, J)
				)

			if not os.path.exists(filename_treat):
				print('Missing treatment file:', filename_treat)
				continue

			if not os.path.exists(filename_control):
				print('Missing control file:', filename_control)
				continue

			df_treat = pd.read_csv(
				filename_treat,
				names=['year', 'stateabbr', 'treatment']
			)

			df_control = pd.read_csv(
				filename_control,
				names=['year', 'stateabbr', 'control']
			)

			df = df_treat.merge(df_control, on=['stateabbr', 'year'])

			df = df.loc[df['stateabbr'].isin(states), :]
			df = df.loc[df['year'].between(FIRSTYEAR, LASTYEAR), :]
			df = df.merge(df_reductions, on=['stateabbr', 'year'], how='left')
			df['reduction'] = df['reduction'].fillna(0.)

			df['treatment'] = df['treatment'] * df['reduction']
			df['control'] = df['control'] * df['reduction']

			index_direct = df['stateabbr'] == stateabbr
			index_indirect = df['stateabbr'] != stateabbr

			if POLICIES == 'none':
				df_results.loc[stateabbr, 'direct'] = df.loc[index_direct, 'treatment'].sum()
			else:
				df_results.loc[stateabbr, 'direct'] = (
					df.loc[index_direct, 'treatment'].sum()
					- df.loc[index_direct, 'control'].sum()
				)

			df_results.loc[stateabbr, 'indirect'] = (
				df.loc[index_indirect, 'treatment'].sum()
				- df.loc[index_indirect, 'control'].sum()
			)

			df_results.loc[stateabbr, 'direct_treatment'] = df.loc[index_direct, 'treatment'].sum()
			df_results.loc[stateabbr, 'direct_control'] = df.loc[index_direct, 'control'].sum()
			df_results.loc[stateabbr, 'indirect_treatment'] = df.loc[index_indirect, 'treatment'].sum()
			df_results.loc[stateabbr, 'indirect_control'] = df.loc[index_indirect, 'control'].sum()

		print(POLICIES, I, J, emission_scenario)
		print(df_results[['direct', 'indirect']].describe())
		print('Share indirect > direct:', (df_results['indirect'] > df_results['direct']).mean())

		## full filename, used for sensitivity plots
		df_results.to_csv(
			os.path.join(
				results_path,
				'emission_reductions_{0:s}_{1:s}_{2:s}_{3:d}_{4:d}.csv'.format(
					emission_scenario, METRIC, POLICIES, I, J
				)
			)
		)

		## backward-compatible filename for existing-policy plots
		if POLICIES != 'none' and I == 5 and J == 9:
			df_results.to_csv(
				os.path.join(
					results_path,
					'emission_reductions_{0:s}_{1:s}_{2:s}.csv'.format(
						emission_scenario, METRIC, POLICIES
					)
				)
			)

		## backward-compatible filename for old none default case
		if POLICIES == 'none' and I == 5 and J == 9:
			df_results.to_csv(
				os.path.join(
					results_path,
					'emission_reductions_{0:s}_{1:s}.csv'.format(
						emission_scenario, METRIC
					)
				)
			)