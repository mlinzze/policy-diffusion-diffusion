#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import string
import pandas as pd
import numpy as np
from copy import deepcopy

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

## ============================================================

from parameters import *

## ============================================================

def file2df(ifile):
	with open(ifile, 'r') as ifp:
		ilines = ifp.readlines()
	n_columns = len(ilines[0].split('&'))
	labels = [l.split(' ')[0] for l in ilines]
	n_variables = labels.index('ll') - 2
	variables = labels[2:n_variables+2]
	df_coeffs = pd.DataFrame(index=variables)
	for i, variable in enumerate(variables):
		line = ilines[2+i]
		coeff, se, p = [str2float(a) for a in line.split('&')[1].split('|')]
		df_coeffs.loc[variable, 'coeff'] = coeff
		df_coeffs.loc[variable, 'se'] = se
		df_coeffs.loc[variable, 'p'] = p
	return df_coeffs.reset_index().rename(columns={'index': 'variable'})

def file2stats(ifile):
	with open(ifile, 'r') as ifp:
		ilines = ifp.readlines()
	n_columns = len(ilines[0].split('&'))
	labels = [l.split(' ')[0] for l in ilines]
	start = labels.index('ll')
	stop = len(labels)
	variables = labels[start:stop]
	df_stats = pd.DataFrame(index=variables)
	for i, variable in enumerate(variables):
		line = ilines[start+i]
		stat = str2float(line.split('&')[1])
		df_stats.loc[variable, 'value'] = stat
	return df_stats.reset_index().rename(columns={'index': 'statistic'})

def str2float(x):
	if x.strip() == '.':
		return np.nan
	else:
		try:
			return float(x)
		except:
			return x

def get_stars(p, mode=1):
	if mode == 0:
		if p < 0.001:
			return '$^{* * *}$'
		elif p < 0.01:
			return '$^{* *}$'
		elif p < 0.05:
			return '$^{*}$'
		else:
			return ''
	elif mode == 1:
		if p < 0.01:
			return '$^{* * *}$'
		elif p < 0.05:
			return '$^{* *}$'
		elif p < 0.1:
			return '$^{*}$'
		else:
			return ''

## ============================================================

df_policy = pd.read_csv(os.path.join(DATAPATH, 'data_policies.csv'))
df_policy = df_policy.sort_values(by=['state', 'year'], ascending=True)
policies = df_policy.drop(columns=['state', 'year']).columns.values

policies_drop = ['environment_preemption_naturalgasbans', 'w_environment_state_nepas_21', 'w_low_income_ee_21']
policies = [p for p in policies if p not in policies_drop]

## ============================================================

df_sectors = pd.read_csv(os.path.join(DATAPATH, 'policygroups.csv'), sep=';')
df_sectors = df_sectors.loc[(df_sectors['Binary coding'] == 1), :]
df_sectors = df_sectors.loc[df_sectors['Policy short'].isin(policies), :]
policies_re = df_sectors.loc[df_sectors['Categories A'].isin(['Renewables', 'Energy']), 'Policy short'].values

## ============================================================

policylabels = list(string.ascii_uppercase[:len(policies)])
policycounts = df_policy.groupby('state').max().reset_index().loc[:, policies].sum(axis=0)
policy2year_avg = {}
policy2year_first = {}
for policy in policies:
	policy2year_avg[policy] = df_policy.loc[df_policy[policy] > 0., :].groupby('state').first()['year'].mean()
	policy2year_first[policy] = df_policy.loc[df_policy[policy] > 0., :].groupby('state').first()['year'].min()

controls = ['gdppc', 'democrat', 'carbonintensity', 'mininggdpshare', 'transutilgdpshare',
			'pctminingempl', 'pcttransutilempl']

## ============================================================

specifications = ['06']
metrics = ['sln', 'sld', 'slg', 'slp', 'slpm']

df_results = pd.DataFrame()

for specification in specifications:
	for metric in metrics:
		for label, policy in zip(policylabels, policies):
			experiment = '{0:s}{1:s}{2:s}'.format(label, specification, metric)
			ifile = os.path.join(RESULTPATH, 'coeffs_{0:s}.txt'.format(experiment))
			if not os.path.exists(ifile):
				print('File not found: ', ifile)
				continue
			df_stats = file2stats(ifile)
			df_stats['specification'] = specification
			df_stats['metric'] = metric
			df_stats['label'] = label
			df_stats['policy'] = policy
			df_stats['npolicies'] = policycounts[policy]
			df_stats['year_avg'] = policy2year_avg[policy]
			df_stats['year_first'] = policy2year_first[policy]
			df_results = pd.concat([df_results, df_stats], axis=0, ignore_index=True)

## ============================================================

indices = (df_results['specification'] == '06') & (df_results['metric'] == 'sld') & (df_results['statistic'] == 'aic')
y1 = df_results.loc[indices, 'value'].values
indices = (df_results['specification'] == '06') & (df_results['metric'] == 'slpm') & (df_results['statistic'] == 'aic')
y2 = df_results.loc[indices, 'value'].values
indices = (df_results['specification'] == '06') & (df_results['metric'] == 'slg') & (df_results['statistic'] == 'aic')
y3 = df_results.loc[indices, 'value'].values
indices = (df_results['specification'] == '06') & (df_results['metric'] == 'sln') & (df_results['statistic'] == 'aic')
y4 = df_results.loc[indices, 'value'].values
indices = (df_results['specification'] == '06') & (df_results['metric'] == 'slp') & (df_results['statistic'] == 'aic')
y5 = df_results.loc[indices, 'value'].values

## ============================================================

indices = (df_results['specification'] == '06') & (df_results['metric'] == 'sld') & (df_results['statistic'] == 'aic') & (df_results['policy'].isin(policies_re))
y1a = df_results.loc[indices, 'value'].values
indices = (df_results['specification'] == '06') & (df_results['metric'] == 'slpm') & (df_results['statistic'] == 'aic') & (df_results['policy'].isin(policies_re))
y2a = df_results.loc[indices, 'value'].values
indices = (df_results['specification'] == '06') & (df_results['metric'] == 'slg') & (df_results['statistic'] == 'aic') & (df_results['policy'].isin(policies_re))
y3a = df_results.loc[indices, 'value'].values
indices = (df_results['specification'] == '06') & (df_results['metric'] == 'sln') & (df_results['statistic'] == 'aic') & (df_results['policy'].isin(policies_re))
y4a = df_results.loc[indices, 'value'].values
indices = (df_results['specification'] == '06') & (df_results['metric'] == 'slp') & (df_results['statistic'] == 'aic') & (df_results['policy'].isin(policies_re))
y5a = df_results.loc[indices, 'value'].values

## ============================================================

indices = (df_results['specification'] == '06') & (df_results['metric'] == 'sld') & (df_results['statistic'] == 'aic') & (~df_results['policy'].isin(policies_re))
y1b = df_results.loc[indices, 'value'].values
indices = (df_results['specification'] == '06') & (df_results['metric'] == 'slpm') & (df_results['statistic'] == 'aic') & (~df_results['policy'].isin(policies_re))
y2b = df_results.loc[indices, 'value'].values
indices = (df_results['specification'] == '06') & (df_results['metric'] == 'slg') & (df_results['statistic'] == 'aic') & (~df_results['policy'].isin(policies_re))
y3b = df_results.loc[indices, 'value'].values
indices = (df_results['specification'] == '06') & (df_results['metric'] == 'sln') & (df_results['statistic'] == 'aic') & (~df_results['policy'].isin(policies_re))
y4b = df_results.loc[indices, 'value'].values
indices = (df_results['specification'] == '06') & (df_results['metric'] == 'slp') & (df_results['statistic'] == 'aic') & (~df_results['policy'].isin(policies_re))
y5b = df_results.loc[indices, 'value'].values

## ============================================================

df_table = pd.DataFrame({'Distance': np.nanpercentile(y1, 50), 'Gravity': np.nanpercentile(y3, 50),
	'Neighbour': np.nanpercentile(y4, 50), 'Party': np.nanpercentile(y2, 50)}, index=[0])

df_table['Policies'] = 'All'
df_table_new = pd.DataFrame({'Policies': 'R/E', 'Distance': np.nanpercentile(y1a, 50), 'Gravity': np.nanpercentile(y3a, 50),
	'Neighbour': np.nanpercentile(y4a, 50), 'Party': np.nanpercentile(y2a, 50)}, index=[0])
df_table = pd.concat([df_table, df_table_new], axis=0)
df_table_new = pd.DataFrame({'Policies': 'Others', 'Distance': np.nanpercentile(y1b, 50), 'Gravity': np.nanpercentile(y3b, 50),
	'Neighbour': np.nanpercentile(y4b, 50), 'Party': np.nanpercentile(y2b, 50)}, index=[0])
df_table = pd.concat([df_table, df_table_new], axis=0)
df_table = df_table.loc[:, ['Policies'] + list(df_table.drop(columns='Policies').columns)]
## end NEW

tablefile = 'table_modelfit.tex'
df_table.to_latex(buf=os.path.join(TABLEPATH, tablefile), index=False, encoding='utf-8',
		float_format="%.1f", escape=False, column_format='r'*(df_table.shape[1]) + 'l', na_rep='')
