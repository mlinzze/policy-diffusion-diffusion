#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import string
import pandas as pd
import numpy as np
from copy import deepcopy

import geopandas as gpd

import scipy.stats
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

## ============================================================

from parameters import *

## ============================================================

SPECIFICATION = '06'
METRIC = 'slpm'

## ============================================================

def file2phtest_p(ifile):
	with open(ifile, 'r') as ifp:
		ilines = ifp.readlines()
	try:
		chisq = float(ilines[-1].split(',')[1].strip())
		df = float(ilines[-1].split(',')[-1].strip())
		p = 1 - scipy.stats.chi2.cdf(chisq, df)
	except:
		print(ilines[-1].split(','))
		return np.nan
	return p

def file2df(ifile):
	with open(ifile, 'r') as ifp:
		ilines = ifp.readlines()
	n_columns = len(ilines[0].split(','))
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

metric2name = {\
	'slp': 'Placebo',
	'sld': 'Distance',
	'slg': 'Gravity',
	'sln': 'Neighbour',
	'slpm': 'Party',
}

variable2name = {
	'log_gdppc': 'log GDP pc',
	'carbonintensity': 'GHG intensity',
	'democrat': 'Democratic control',
	'pctminingempl': 'Employment in mining (%)',
	'pcttransutilempl': 'Employment in transport and utilities (%)',
	'mininggdpshare': 'GDP of mining (%)',
	'transutilgdpshare': 'GDP of transport and utilities (%)',
	'popdens': 'Population density',
	'log_poptotal': 'log Population',
	'log_area': 'log Land area',
	'wind': 'Wind power potential',
	'solar': 'Solar power potential',
	'coal': 'Coal production',
	'share_evangelical': 'Share evangelical',
	'climate_concern': 'Concern about climate change'
}

## ============================================================

df_policy = pd.read_csv(os.path.join(DATAPATH, 'data_policies.csv'))
df_policy = df_policy.sort_values(by=['state', 'year'], ascending=True)
policies = df_policy.drop(columns=['state', 'year']).columns.values

policies_drop = ['environment_preemption_naturalgasbans', 'w_environment_state_nepas_21', 'w_low_income_ee_21']
policies = [p for p in policies if p not in policies_drop]

policylabels = list(string.ascii_uppercase[:len(policies)])
policycounts = df_policy.groupby('state').max().reset_index().loc[:, policies].sum(axis=0)
policy2year_avg = {}
policy2year_first = {}
for policy in policies:
	policy2year_avg[policy] = df_policy.loc[df_policy[policy] > 0., :].groupby('state').first()['year'].mean(numeric_only=True)
	policy2year_first[policy] = df_policy.loc[df_policy[policy] > 0., :].groupby('state').first()['year'].min(numeric_only=True)

controls = ['pc{0:02d}'.format(i) for i in range(1, 6+1, 1)]

## ============================================================

metrics = ['slp', 'slpm']

df_results = pd.DataFrame()

for metric in metrics:
	if metric == 'slpm':
		specifications = ['06']
	elif metric == 'slp':
		specifications = ['00', '06']
	for specification in specifications:
		for label, policy in zip(policylabels, policies):
			experiment = '{0:s}{1:s}{2:s}'.format(label, specification, metric)
			ifile = os.path.join(RESULTPATH, 'coeffs_{0:s}.txt'.format(experiment))
			if not os.path.exists(ifile):
				print('File not found: ', ifile)
				df_coeffs = pd.DataFrame({'variable': '{0:s}_{1:s}'.format(policy, metric), 'coeff': np.nan, 'se': np.nan}, index=[0])
			else:
				df_coeffs = file2df(ifile)
			df_coeffs['specification'] = specification
			df_coeffs['metric'] = metric
			df_coeffs['label'] = label
			df_coeffs['policy'] = policy
			df_coeffs['npolicies'] = policycounts[policy]
			df_coeffs['year_avg'] = policy2year_avg[policy]
			df_coeffs['year_first'] = policy2year_first[policy]

			ifile = os.path.join(RESULTPATH, 'phtest_{0:s}.txt'.format(experiment))
			if not os.path.exists(ifile):
				p = np.nan
			else:
				p = file2phtest_p(ifile)
			df_coeffs['phtest_p'] = p

			df_results = pd.concat([df_results, df_coeffs], axis=0, ignore_index=True)

df_results['sig'] = df_results['p'] < 0.05
df_results['stars'] = df_results['p'].apply(lambda x: get_stars(x, mode=1))
df_results['spatial_lag'] = df_results['variable'].apply(lambda x: x.split('_')[-1] in metrics)
df_results['phtest_fail'] = df_results['phtest_p'] < 0.1

## ============================================================

df_sectors = pd.read_csv(os.path.join(DATAPATH, 'policygroups.csv'), sep=';')
df_sectors = df_sectors.loc[(df_sectors['Binary coding'] == 1), :]
df_sectors = df_sectors.loc[df_sectors['Policy short'].isin(policies), :]
policies_re = df_sectors.loc[df_sectors['Categories A'].isin(['Renewables', 'Energy']), 'Policy short'].values
df_results['re'] = df_results['policy'].isin(policies_re)
df_results['other'] = ~df_results['re']

## ============================================================

dfz = df_results.loc[df_results['spatial_lag'], :]

dfz.groupby(['specification'])['coeff'].count()

print('Failed test: ', dfz.loc[dfz['metric'] == METRIC, :].groupby(['specification'])['phtest_fail'].sum())

for metric in metrics:
	if metric == 'slpm':
		specifications = ['06']
	elif metric == 'slp':
		specifications = ['00', '06']
	for specification in specifications:
		if metric == 'slp':
			samples = ['all']
		else:
			samples = ['all', 're', 'other']
		for sample in samples:
			if sample == 'all':
				dfs = dfz.copy()
			if sample == 're':
				dfs = dfz.loc[dfz['re'], :]
			if sample == 'other':
				dfs = dfz.loc[dfz['other'], :]

			#if (specification != SPECIFICATION) & (metric not in ['slp', METRIC]):
			#	continue
			dfzz = dfs.loc[dfs['metric'] == metric, :]
			dfzz = dfzz.loc[dfzz['specification'] == specification, :]
			dfzz = dfzz.loc[dfzz['phtest_fail'] == False, :]

			yvals = dfzz.apply(lambda x: np.random.normal(loc=x['coeff'], scale=x['se'], size=1000), axis=1).explode().values

			fig, ax = plt.subplots(figsize=(6, 4))
			sns.distplot(yvals, bins=np.arange(-20., 20.+1, 1))
			ylims = ax.get_ylim()
			ax.plot([0., 0.], ylims, 'k-')
			ax.plot([np.nanpercentile(yvals, 50)]*2, ylims, 'r--')
			ax.set_ylim(ylims)
			ax.set_ylabel('Frequency')
			ax.set_xlabel('Diffusion coefficient')
			ax.set_xlim(-20., 20.)
			sns.despine(ax=ax, offset=1., right=True, top=True)
			#ax.annotate(text=r"Metric: {0:s}, median: {1:3.2f}, mean: {2:3.2f}".format(metric2name[metric], np.nanpercentile(yvals, 50), np.nanmean(yvals)),
			#		xy=(0., 1.05), xycoords='axes fraction', ha='left', va='bottom')
			ax.annotate(text="Metric: {0:s}\nMedian: {1:3.2f}".format(metric2name[metric], np.nanpercentile(yvals, 50)),
					xy=(0.05, 1.0), xycoords='axes fraction', ha='left', va='top')
			ax.annotate(text="IQR: [{0:3.2f}, {1:3.2f}]".format(np.nanpercentile(yvals, 25), np.nanpercentile(yvals, 75)),
					xy=(0.05, 0.89), xycoords='axes fraction', ha='left', va='top')
			fig.savefig(os.path.join(FIGUREPATH, 'coeffs_distribution_{0:s}_{1:s}_{2:s}.pdf'.format(specification, metric, sample)), bbox_inches='tight', transparent=True)

			if (specification == SPECIFICATION) & (metric == METRIC):
				print('## ================================================================================ ##')
				print('Estimated coefficient of spatial lag: {0:6.5f}'.format(np.nanpercentile(yvals, 50)))
				print('## ================================================================================ ##')

#print(dfz.corr().loc['npolicies', 'coeff'])

## ========================================================================================================================
## examine explanatory variable of covariates, using estimated coefficients of PCA from Cox model

df_expl = pd.read_csv('./data/data_merged_pca.csv')
df_expl = df_expl.sort_values(by=['stateabbr', 'year'], ascending=True, ignore_index=True)
df_last = df_expl.groupby('stateabbr').last().reset_index()
df_last.columns = [c.lower() for c in df_last.columns]
variables = ['log_gdppc', 'carbonintensity', 'democrat',
					'pctminingempl', 'pcttransutilempl', 'mininggdpshare', 'transutilgdpshare',
					'popdens', 'log_poptotal', 'log_area',
					'wind', 'solar', 'coal',
					'share_evangelical', 'climate_concern']
pca_variables = ['pc{0:02d}'.format(i) for i in range(1, len(variables)+1, 1)]

df_all = pd.DataFrame()

dfz = df_results.loc[(df_results['specification'] == SPECIFICATION) & (~df_results['spatial_lag']) & (df_results['metric'] == METRIC), :]

for policy in df_results['policy'].unique():
	df_temp = df_last.copy()
	df_temp['policy'] = policy

	dfzz = dfz.loc[(dfz['policy'] == policy), ['variable', 'coeff']].set_index('variable')
	df_temp['predicted'] = (df_temp.loc[:, dfzz.index.values] * dfzz['coeff']).sum(axis=1)
	df_all = pd.concat([df_all, df_temp], ignore_index=True, axis=0)

dfm = df_all.groupby('state').mean(numeric_only=True).reset_index()

dfm_re = df_all.loc[df_all['policy'].isin(policies_re), :].groupby('state').mean(numeric_only=True).reset_index()
dfm_others = df_all.loc[~df_all['policy'].isin(policies_re), :].groupby('state').mean(numeric_only=True).reset_index()

scaler = StandardScaler()
dfm.loc[:, variables] = scaler.fit_transform(dfm.loc[:, variables])
dfm_re.loc[:, variables] = scaler.fit_transform(dfm_re.loc[:, variables])
dfm_others.loc[:, variables] = scaler.fit_transform(dfm_others.loc[:, variables])

## ========================================================================================================================

import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.linear_model import Lasso

# with OLS
formula = 'predicted ~ {0:s}'.format(' + '.join(variables))
model = sm.OLS.from_formula(formula, dfm).fit(missing='drop').get_robustcov_results()
dx = model.summary2(float_format="%.5f").tables[1].iloc[:, [0, 1, 3]]
dfm['yhat'] = model.predict(dfm.loc[:, variables])
dfm['exp_yhat'] = np.exp(dfm['yhat'])
dfm['prob'] = dfm['exp_yhat'] / dfm['exp_yhat'].mean(numeric_only=True) * 0.05

# with Lasso
model = Lasso(alpha=0.5, max_iter=10000)
model.fit(dfm.loc[:, variables], dfm.loc[:, 'predicted'])
selected_variables = [var for var, coef in zip(variables, model.coef_.flatten()) if coef != 0]
formula = 'predicted ~ {0:s}'.format(' + '.join(selected_variables))
model = sm.OLS.from_formula(formula, dfm).fit(missing='drop').get_robustcov_results()
dx = model.summary2(float_format="%.5f").tables[1].iloc[:, [0, 1, 3]]
dfm['yhat'] = model.predict(dfm.loc[:, selected_variables])
dfm['exp_yhat'] = np.exp(dfm['yhat'])
dfm['prob'] = dfm['exp_yhat'] / dfm['exp_yhat'].mean(numeric_only=True) * 0.05 * 100.
pd.DataFrame(selected_variables, columns=['variable']).to_csv(os.path.join(RESULTPATH, 'covariates.csv'), index=False)

## by policy group
formula = 'predicted ~ {0:s}'.format(' + '.join(selected_variables))
model = sm.OLS.from_formula(formula, dfm_re).fit(missing='drop').get_robustcov_results()
dx_re = model.summary2(float_format="%.5f").tables[1].iloc[:, [0, 1, 3]]

formula = 'predicted ~ {0:s}'.format(' + '.join(selected_variables))
model = sm.OLS.from_formula(formula, dfm_others).fit(missing='drop').get_robustcov_results()
dx_others = model.summary2(float_format="%.5f").tables[1].iloc[:, [0, 1, 3]]

## ========================================================================================================================

def extract_errorbar(dx, variable):
	estimate = dx.loc[variable, 'Coef.']
	error = 1.96*dx.loc[variable, 'Std.Err.']
	return estimate, error

dx = dx.sort_values(by=['Coef.'], ascending=False)
dx = dx.loc[dx.index != 'Intercept', :]
dx.reset_index().rename(columns={'Coef.': 'coeff', 'index': 'variable', 'Std.Err.': 'se'}).loc[:, ['variable', 'coeff', 'se']].to_csv('coefficients_covariates.csv', index=False)

fig, ax = plt.subplots(figsize=(5,5))
y = 0.
for variable in dx.index.values:
	x, x_error = extract_errorbar(dx, variable)
	ax.errorbar(x, y, xerr=x_error, lw=3., color='grey')
	ax.plot(x, y, 'ko', markersize=8); y -= 1.
ax.set_yticks(np.arange(y+1, 0.+1, 1.))
ax.set_yticklabels([variable2name.get(v) for v in dx.index.values[::-1]])
ylims = ax.get_ylim()
ax.plot([0., 0.], ylims, 'k--')
ax.set_ylim(ylims)
sns.despine(ax=ax, offset=1., right=True, top=True)
ax.set_xlabel('Estimated coefficient (standardised)')
#ax.legend()
fig.savefig(os.path.join(FIGUREPATH, 'coefficients_covariates.pdf'), bbox_inches='tight', transparent=True)

## ===================

dx_re = dx_re.sort_values(by=['Coef.'], ascending=False)
dx_re = dx_re.loc[dx_re.index != 'Intercept', :]
dx_re.reset_index().rename(columns={'Coef.': 'coeff', 'index': 'variable', 'Std.Err.': 'se'}).loc[:, ['variable', 'coeff', 'se']].to_csv('coefficients_covariates.csv', index=False)
dx_others = dx_others.sort_values(by=['Coef.'], ascending=False)
dx_others = dx_others.loc[dx_others.index != 'Intercept', :]
dx_others.reset_index().rename(columns={'Coef.': 'coeff', 'index': 'variable', 'Std.Err.': 'se'}).loc[:, ['variable', 'coeff', 'se']].to_csv('coefficients_covariates.csv', index=False)

fig, ax = plt.subplots(figsize=(5,5))
y = 0.
for variable in dx.index.values:
	x, x_error = extract_errorbar(dx, variable)
	ax.errorbar(x, y, xerr=x_error, lw=3., color='grey')
	ax.plot(x, y, 'ko', markersize=8); y -= 0.2

	x, x_error = extract_errorbar(dx_re, variable)
	ax.errorbar(x, y, xerr=x_error, lw=3., color='green', alpha=0.6)
	ax.plot(x, y, 'go', markersize=8); y -= 0.2

	x, x_error = extract_errorbar(dx_others, variable)
	ax.errorbar(x, y, xerr=x_error, lw=3., color='blue', alpha=0.6)
	ax.plot(x, y, 'bo', markersize=8); y -= 0.6

from matplotlib.lines import Line2D
point1 = Line2D([0], [0], label='All policies', marker='o', markersize=8, 
	markeredgecolor='k', markerfacecolor='k', linestyle='')
point2 = Line2D([0], [0], label='R/E policies', marker='o', markersize=8, 
	markeredgecolor='g', markerfacecolor='g', linestyle='')
point3 = Line2D([0], [0], label='Other policies', marker='o', markersize=8, 
	markeredgecolor='b', markerfacecolor='b', linestyle='')
ax.legend(handles=[point1, point2, point3])

ax.set_yticks(np.arange(y+1, 0.+1, 1.))
ax.set_yticklabels([variable2name.get(v) for v in dx.index.values[::-1]])
ylims = ax.get_ylim()
ax.plot([0., 0.], ylims, 'k--')
ax.set_ylim(ylims)
sns.despine(ax=ax, offset=1., right=True, top=True)
ax.set_xlabel('Estimated coefficient (standardised)')
#ax.legend()
fig.savefig(os.path.join(FIGUREPATH, 'coefficients_covariates_policygroups.pdf'), bbox_inches='tight', transparent=True)

## ========================================================================================================================

# read in shapes
datapath = "./data/shapes"
datafile = "cb_2018_us_state_20m.shp"
gdf_shapes = gpd.read_file(os.path.join(datapath, datafile))
gdf = gdf_shapes.merge(dfm, left_on=['NAME'], right_on=['state'], how='left')

bounds = [0., 0.1, 0.5, 1, 5, 10, 25]

extend = 'max'
formatcode = '%.1f'
fig, ax = plt.subplots(figsize=(5,5))
cmap = plt.cm.Greens
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
ax2 = fig.add_axes([0.95, 0.25, 0.03, 0.5])
cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm,
	spacing='uniform', ticks=bounds, boundaries=bounds, format=formatcode, label='Probability (percent)', extend=extend)#{0:s}'.format(variable.replace('_', ' before '))
gdf.plot(ax=ax, facecolor='k', alpha=0.1, ec='k', lw=0.5)
gdf.plot(ax=ax, column='prob', cmap=cmap, norm=norm, vmin=bounds[0], vmax=bounds[-1], markersize=0.02, facecolor='k', marker='o', ec='k', lw=0.5)
ax.set_xlabel('Longitude (degrees)')
ax.set_ylabel('Latitude (degrees)')
ax.set_xlim(-127., -64.)
ax.set_ylim(23., 50.)
ax.set_title('Covariate-adjusted baseline probability of policy adoption', size='small')
fig.savefig(os.path.join(FIGUREPATH, 'geomap_baseline.png'), bbox_inches='tight', dpi=500)
