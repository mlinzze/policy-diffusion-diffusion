## ============================
## plot effect of initial adopters
## ============================
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import copy
import itertools
import numpy as np
import pandas as pd
import random
import geopandas as gpd

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

## ============================================================

from parameters import *

## ============================

METRIC = 'slpm'
POLICIES = 'none'

SIMULATIONS_PATH = './simulations'
EXPERIMENT = 'results_{0:s}_linear_future_2050_{1:s}'.format(METRIC, POLICIES)

## ============================

COLOR1 = 'b'
COLOR2 = 'r'
COLOR3 = 'm'
COLOR4 = 'c'
COLOR5 = 'g'

label = EXPERIMENT

## ============================
## plot scatter
## ============================

emission_scenario = 'constant'

results_path = os.path.join(SIMULATIONS_PATH, EXPERIMENT)
if POLICIES != 'none':
	df_results = pd.read_csv(os.path.join(results_path, 'emission_reductions_{0:s}_{1:s}_{2:s}.csv'.format(emission_scenario, METRIC, POLICIES)))
else:
	df_results = pd.read_csv(os.path.join(results_path, 'emission_reductions_{0:s}_{1:s}.csv'.format(emission_scenario, METRIC)))

df_results['indirect_larger'] = df_results['indirect'] > df_results['direct']
df_results['factor'] = df_results['indirect'] / df_results['direct']
print('Indirect larger than direct, GHG :', df_results['indirect_larger'].sum() / df_results['direct'].count())

## ============================

df_results = df_results.set_index('stateabbr')

ylims = [130., 390.]

fig, ax = plt.subplots(figsize=(5,4))
for iso in df_results.index.values:
	x = df_results.loc[iso, 'direct']
	y = df_results.loc[iso, 'indirect']
	ax.plot(x, y, color='white')
	ax.annotate(text='{0:s}'.format(iso), xy=(x, y), xycoords='data', ha='center', va='center', size='small', color='black', alpha=0.6)
	if y > np.max(ylims):
		ax.annotate(text='{0:s} = {1:.0f}'.format(iso, y), xy=(x, ylims[1]), xycoords='data', ha='center', va='top', size='small', color='black', alpha=1.)
	if y < np.min(ylims):
		ax.annotate(text='{0:s} = {1:.0f}'.format(iso, y), xy=(x, ylims[0]), xycoords='data', ha='center', va='bottom', size='small', color='black', alpha=1.)
ax.set_xlabel('Direct emission reductions (Mt CO2eq)')
ax.set_ylabel('Indirect emission red. (Mt CO2eq)')
#ax.set_ylim(9e-3, 0.6)
ax.set_xscale('log')
ax.set_yscale('log')
xlims = ax.get_xlim()
#ylims = ax.get_ylim()
ax.plot([0., 0.], ylims, 'k-', lw=0.5)
ax.plot(np.linspace(0., ylims[-1], 1000), np.linspace(0., ylims[-1], 1000), 'k--')
ax.set_ylim(ylims)
ax.set_xlim(xlims)
sns.despine(ax=ax, offset=1., right=True, top=True)
ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%.0f'))
ax.yaxis.set_major_formatter(mpl.ticker.FormatStrFormatter('%.0f'))
ax.yaxis.set_minor_formatter(mpl.ticker.FormatStrFormatter('%.0f'))
fig.savefig(os.path.join(FIGUREPATH, 'scatter_indirect_{0:s}.pdf'.format(EXPERIMENT)), bbox_inches='tight', dpi=300., transparent=True)
fig.savefig(os.path.join(FIGUREPATH, 'scatter_indirect_{0:s}.png'.format(EXPERIMENT)), bbox_inches='tight', dpi=300., transparent=True)

## ============================
## plot effect of initial adopters
## ============================

emission_scenario = 'constant'

POLICIES_LIST = ['0', '1', '3', '5', '10', '20', '30']

rows = []

for policies in POLICIES_LIST:

	experiment = 'results_{0:s}_linear_future_2050_{1:s}'.format(METRIC, policies)
	results_path = os.path.join(SIMULATIONS_PATH, experiment)

	if policies == 'none':
		n_existing_policies = 0
	else:
		n_existing_policies = int(policies)

	df_emissions = pd.read_csv(
		os.path.join(
			results_path,
			'emission_reductions_{0:s}_{1:s}_{2:s}.csv'.format(emission_scenario, METRIC, policies)
		)
	)

	for _, row in df_emissions.iterrows():
		rows.append({
			'policies': policies,
			'n_existing_policies': n_existing_policies,
			'stateabbr': row['stateabbr'],
			'indirect': row['indirect']
		})

df_box = pd.DataFrame(rows)
df_box = df_box.sort_values(by=['n_existing_policies', 'stateabbr']).reset_index(drop=True)

print(
	df_box
	.groupby('n_existing_policies')['indirect']
	.describe(percentiles=[0.025, 0.25, 0.5, 0.75, 0.975])
)

## ============================
## figure
## ============================

x_values = sorted(df_box['n_existing_policies'].unique())
positions = np.arange(1, len(x_values) + 1)

data = [
	df_box.loc[df_box['n_existing_policies'] == x, 'indirect'].values
	for x in x_values
]

fig, ax = plt.subplots(figsize=(5,4))

bp = ax.boxplot(
	data,
	positions=positions,
	widths=0.55,
	whis=[2.5, 97.5],
	showmeans=True,
	showfliers=False,
	patch_artist=True,
	medianprops={'color': 'black', 'lw': 1.4},
	meanprops={
		'marker': 'o',
		'markerfacecolor': 'white',
		'markeredgecolor': 'black',
		'markersize': 4
	},
	boxprops={
		'facecolor': 'lightgrey',
		'edgecolor': 'black',
		'lw': 1.
	},
	whiskerprops={
		'color': 'black',
		'lw': 1.
	},
	capprops={
		'color': 'black',
		'lw': 1.
	}
)

ax.axhline(0., color='black', lw=0.6)

ax.set_xlabel('Number of existing policies in 2024')
ax.set_ylabel('Indirect emission reductions\nby state (Mt CO2eq)')

ax.set_xticks(positions)
ax.set_xticklabels([str(x) for x in x_values])

sns.despine(ax=ax, offset=1., right=True, top=True)

fig.savefig(
	os.path.join(FIGUREPATH, 'boxplot_indirect_emissions_existing_policies_{0:s}_{1:s}.pdf'.format(METRIC, emission_scenario)),
	bbox_inches='tight',
	dpi=300.,
	transparent=True
)

fig.savefig(
	os.path.join(FIGUREPATH, 'boxplot_indirect_emissions_existing_policies_{0:s}_{1:s}.png'.format(METRIC, emission_scenario)),
	bbox_inches='tight',
	dpi=300.,
	transparent=True
)