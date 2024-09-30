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

def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
	new_cmap = mpl.colors.LinearSegmentedColormap.from_list(
		'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
		cmap(np.linspace(minval, maxval, n)))
	return new_cmap

## ============================

METRIC = 'slpm'
SIMULATIONS_PATH = './simulations'
EXPERIMENT = 'results_{0:s}_linear_future_2050_none'.format(METRIC)

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

scenario = 'constant'

results_path = os.path.join(SIMULATIONS_PATH, EXPERIMENT)
df_results = pd.read_csv(os.path.join(results_path, 'solar_expansion_{0:s}_{1:s}.csv'.format(scenario, METRIC)))

## ============================

df_results['capacity_direct'] = df_results['capacity_direct'] # in MW
df_results['capacity_indirect'] = df_results['capacity_indirect'] # in MW

df_results['emissions_direct'] = df_results['emissions_direct'] / 1.e6 # in Mt
df_results['emissions_indirect'] = df_results['emissions_indirect'] / 1.e6 # in Mt

## ============================

df_results['emissions_indirect_larger'] = df_results['emissions_indirect'] > df_results['emissions_direct']
df_results['emissions_factor'] = df_results['emissions_indirect'] / df_results['emissions_direct']
print('Indirect larger than direct, GHG from solar :', df_results['emissions_indirect_larger'].sum() / df_results['emissions_direct'].count())
df_results['capacity_indirect_larger'] = df_results['capacity_indirect'] > df_results['capacity_direct']
df_results['capacity_factor'] = df_results['capacity_indirect'] / df_results['capacity_direct']
print('Indirect larger than direct, solar capacity:', df_results['capacity_indirect_larger'].sum() / df_results['capacity_direct'].count())

## ============================

df_results = df_results.set_index('stateabbr')

ylims = np.array([80, 160])

fig, ax = plt.subplots(figsize=(5,4))
for iso in df_results.index.values:
	x = df_results.loc[iso, 'capacity_direct']
	y = df_results.loc[iso, 'capacity_indirect']
	ax.plot(x, y, color='white')
	ax.annotate(text='{0:s}'.format(iso), xy=(x, y), xycoords='data', ha='center', va='center', size='small', color='black', alpha=0.6)
	if y > np.max(ylims):
		ax.annotate(text='{0:s} = {1:.0f}'.format(iso, y), xy=(x, ylims[1]), xycoords='data', ha='center', va='top', size='small', color='black', alpha=1.)
	if y < np.min(ylims):
		ax.annotate(text='{0:s} = {1:.0f}'.format(iso, y), xy=(x, ylims[0]), xycoords='data', ha='center', va='bottom', size='small', color='black', alpha=1.)
ax.set_xlabel('Direct generation capacity (MW)')
ax.set_ylabel('Indirect generation capacity (MW)')
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
fig.savefig(os.path.join(FIGUREPATH, 'scatter_solar_indirect_capacity_{0:s}.pdf'.format(EXPERIMENT)), bbox_inches='tight', dpi=300., transparent=True)
fig.savefig(os.path.join(FIGUREPATH, 'scatter_solar_indirect_capacity_{0:s}.png'.format(EXPERIMENT)), bbox_inches='tight', dpi=300., transparent=True)

## ============================

ylims = np.array([1.5, 5.])

fig, ax = plt.subplots(figsize=(5,4))
for iso in df_results.index.values:
	x = df_results.loc[iso, 'emissions_direct']
	y = df_results.loc[iso, 'emissions_indirect']
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
fig.savefig(os.path.join(FIGUREPATH, 'scatter_solar_indirect_emissions_{0:s}.pdf'.format(EXPERIMENT)), bbox_inches='tight', dpi=300., transparent=True)
fig.savefig(os.path.join(FIGUREPATH, 'scatter_solar_indirect_emissions_{0:s}.png'.format(EXPERIMENT)), bbox_inches='tight', dpi=300., transparent=True)

## ============================
## plot map
## ============================

dfs = pd.read_csv(os.path.join(DATAPATH, 'states.csv'))
dfr = df_results.reset_index().merge(dfs, on='stateabbr', how='left')

# read in shapes
datapath = os.path.join(DATAPATH, "shapes")
datafile = "cb_2018_us_state_20m.shp"
gdf_states = gpd.read_file(os.path.join(datapath, datafile))
gdf = gdf_states.merge(dfr, left_on=['NAME'], right_on=['state'], how='left')
gdf.loc[gdf['state'].isnull(), 'NAME']

bounds = np.arange(1, 5.5, 0.5)

extend = 'both'
formatcode = '%.1f'
fig, ax = plt.subplots(figsize=(10,6))
cmap = plt.cm.Greens
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
ax2 = fig.add_axes([0.95, 0.25, 0.03, 0.5])
cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm,
	spacing='uniform', ticks=bounds, boundaries=bounds, format=formatcode, label='Indirect emission reductions (Mt CO2eq)', extend=extend)#{0:s}'.format(variable.replace('_', ' before '))
gdf.plot(ax=ax, facecolor='k', alpha=0.1, ec='k', lw=0.5)
gdf.plot(ax=ax, facecolor='k', alpha=0.4, ec='k', lw=0.5)
gdf.plot(ax=ax, column='emissions_indirect', cmap=cmap, norm=norm, vmin=bounds[0], vmax=bounds[-1], markersize=0.02, facecolor='k', marker='o', ec='k', lw=0.5)
ax.set_xlabel('Longitude (degrees)')
ax.set_ylabel('Latitude (degrees)')
ax.set_xlim(-127., -64.)
ax.set_ylim(23., 50.)
fig.savefig(os.path.join(FIGUREPATH, 'geomap_solar_indirect_emissions_{0:s}.png'.format(EXPERIMENT)), bbox_inches='tight', dpi=200)
