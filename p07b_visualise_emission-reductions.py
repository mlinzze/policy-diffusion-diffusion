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

emission_scenario = 'constant'

results_path = os.path.join(SIMULATIONS_PATH, EXPERIMENT)
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