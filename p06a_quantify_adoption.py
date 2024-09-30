#!/usr/bin/env python

import os
import numpy as np
import pandas as pd
from copy import deepcopy

import geopandas as gpd

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

## ============================================================

from parameters import *

## ============================== ##

def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
	new_cmap = mpl.colors.LinearSegmentedColormap.from_list(
		'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
		cmap(np.linspace(minval, maxval, n)))
	return new_cmap

cmap = truncate_colormap(plt.cm.Greens, minval=40., maxval=100.)
cmap.set_under('grey')
try:
	mpl.cm.register_cmap("custom_cmap", cmap)
except:
	pass

## ============================== ##

probabilities = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
beta_Ws = [0., 1., 2., 3., 4., 5.]

BETA_W = 1.95

def get_beta_Ws(j):
	if j != 9:
		return beta_Ws[j]
	else:
		return BETA_W

## ============================== ##

states = pd.read_csv('./simulations/states.csv').iloc[:, 0].values

## ============================== ##

METRIC = 'slpm'
YEARS = np.arange(2024, 2050+1, 1)

## ============================== ##

df_all = pd.DataFrame()

for i in range(1, 10+1, 1): # constant
	for j in list(range(0, 5+1, 1)) + [9]: # beta_W
		results_path = './simulations/results_{0:s}_linear_future_2050_none'.format(METRIC)
		if not os.path.exists(results_path):
			print('Path does not exist: ', results_path)
			continue

		df = pd.read_csv(os.path.join(results_path, 'result_{0:s}_0_{1:d}_{2:d}.csv'.format('ANY', i, j)), names=['year', 'state', 'p'])
		df['p'] = df.groupby('state')['p'].cumsum(axis=0)

		for year in YEARS:

			n = df.loc[df['year'] == year, 'p'].sum(axis=0)
			df_all = pd.concat([df_all,
					pd.DataFrame({'year': year, 'n': n, 'i': i, 'j': j}, index=[0])], ignore_index=True)

df_all['prob'] = df_all['i'].apply(lambda x: probabilities[x-1])
df_all['beta_W'] = df_all['j'].apply(lambda x: get_beta_Ws(x))

## ============================== ##

# all in percentage
df_all['n'] = df_all['n'] / 50. * 100.
df_all['prob'] = df_all['prob'] * 100.

## ============================== ##

linestyles = ['-', '--']

for i, year in enumerate([2030, 2050]):

	fig, ax = plt.subplots()

	linestyle = linestyles[0]
	dfm = df_all.loc[df_all['year'] == year, :]

	dfs = dfm.loc[dfm['j'] == 0, :]
	x = dfs['prob'].values
	y = dfs['n'].values
	ax.plot(x, y, 'bo', label='beta W = 0', linestyle=linestyle)
	dfs = dfm.loc[dfm['j'] == 1, :]
	x = dfs['prob'].values
	y = dfs['n'].values
	ax.plot(x, y, 'ko', label='beta W = 1', linestyle=linestyle)
	dfs = dfm.loc[dfm['j'] == 9, :]
	x = dfs['prob'].values
	y = dfs['n'].values
	ax.plot(x, y, 'ro', label='beta W = {0:3.2f}'.format(BETA_W), linestyle=linestyle)
	dfs = dfm.loc[dfm['j'] == 2, :]
	x = dfs['prob'].values
	y = dfs['n'].values
	ax.plot(x, y, 'go', label='beta W = 2', linestyle=linestyle)
	dfs = dfm.loc[dfm['j'] == 3, :]
	x = dfs['prob'].values
	y = dfs['n'].values
	ax.plot(x, y, 'mo', label='beta W = 3', linestyle=linestyle)
	ax.legend()
	ax.set_xlabel('Baseline hazard (percent)')
	ax.set_ylabel('Adoption of policy in {0:d} (percent of states)'.format(year))
	sns.despine(ax=ax, offset=1., right=True, top=True)
	fig.savefig(os.path.join(FIGUREPATH, 'lines_sensitivity_{0:d}.pdf'.format(year)), bbox_inches='tight', dpi=300., transparent=True)

## ============================== ##

dfm = df_all.loc[df_all['prob'] == 5, :]

fig, ax = plt.subplots(figsize=(6,5))

dfs = dfm.loc[dfm['j'] == 0, :]
x = dfs['year'].values
y = dfs['n'].values
ax.plot(x, y, 'b', label=r'$\beta_{W}$ = 0 (no diffusion)', linestyle='-')
dfs = dfm.loc[dfm['j'] == 1, :]
x = dfs['year'].values
y = dfs['n'].values
ax.plot(x, y, 'k', label=r'$\beta_{W}$ = 1', linestyle='-')
dfs = dfm.loc[dfm['j'] == 9, :]
x = dfs['year'].values
y = dfs['n'].values
ax.plot(x, y, 'r', label=r'$\beta_{W}$' + ' = {0:3.2f}'.format(BETA_W), linestyle='--')
dfs = dfm.loc[dfm['j'] == 4, :]
x = dfs['year'].values
y = dfs['n'].values
ax.plot(x, y, 'm', label=r'$\beta_{W}$ = 4', linestyle='-')
ax.legend()
ax.set_xlabel('Year')
ax.set_ylabel('Adoption of policy in {0:d} (percent of states)'.format(year))
sns.despine(ax=ax, offset=1., right=True, top=True)
fig.savefig(os.path.join(FIGUREPATH, 'lines_timeseries.pdf'), bbox_inches='tight', dpi=300., transparent=True)

## ============================== ##

for year in [2030, 2050]:

	dfm = df_all.loc[df_all['year'] == year, :]
	dfm = dfm.loc[dfm['j'] != 9]
	dfm['label'] = dfm['n'].apply(lambda x: '{0:2.0f}'.format(x))

	def plotlabel(xvar, yvar, label, color='k'):
		ax.text(xvar, yvar, label, ha='center', va='center', size='large', color=color)
 	
	cmap = plt.cm.Greens

	fig, ax = plt.subplots(figsize=(6,5))
	sns.scatterplot(ax=ax, data=dfm, x='prob', y='beta_W', hue='n',
			palette=cmap, legend=False, s=1000)
	dfm.loc[dfm['n'] < 80., :].apply(lambda x: plotlabel(x['prob'], x['beta_W'], x['label'], color='k'), axis=1)
	dfm.loc[dfm['n'] >= 80., :].apply(lambda x: plotlabel(x['prob'], x['beta_W'], x['label'], color='w'), axis=1)
	#ax.plot(1., 1., marker='o', markersize=40, markeredgecolor='r', markerfacecolor='none')
	ax.plot([dfm['prob'].min()-0.5, dfm['prob'].max()+0.5], [BETA_W, BETA_W], 'r--', label=r'Empirical estimate of $\beta_{W}$')
	ax.annotate(text=r'Empirical estimate of $\beta_{W}$: ' + '{0:3.2f}'.format(BETA_W), xy=(10., BETA_W-0.3), ha='right', va='top', color='r', xycoords='data')
	ax.set_xlabel('Mean baseline hazard (percent)')
	ax.set_ylabel(r'Diffusion parameter $\beta_{W}$')
	ax.set_title('Percentage of states with policy by {0:d}'.format(year))
	ax.set_xlim(0., 10.5)
	ax.set_ylim(-0.5, 5.5)
	sns.despine(ax=ax, offset=1., right=True, top=True)
	fig.savefig(os.path.join(FIGUREPATH, 'scatter_sensitivity_{0:d}.pdf'.format(year)), bbox_inches='tight', dpi=300., transparent=True)

## ========================================================================================== ##
