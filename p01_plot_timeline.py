#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

## ============================================================

from parameters import *

## ============================================================

df = pd.read_csv(os.path.join(DATAPATH, 'data_policies.csv'))
df = df.sort_values(by=['state', 'year'], ascending=True, ignore_index=True)
policies = df.drop(columns=['state', 'year']).columns.values

for policy in policies:
	df[policy] = (df.groupby('state')[policy].diff() > 0.).astype(int)

df = df.merge(df_states, on='state', how='left')
df = df.loc[df['year'] >= 1980, :]

## ============================================================

dfs = pd.read_csv(os.path.join(DATAPATH, 'data_policies.csv'))
dfs = dfs.sort_values(by=['state', 'year'], ascending=True, ignore_index=True)
for policy in policies:
	dfs[policy] = dfs.loc[dfs[policy] == 1, 'year'].min()
sequence = dfs.iloc[0, 2:].sort_values().index.values
df_states = pd.read_csv(os.path.join(DATAPATH, 'states.csv'))

## ============================================================

df_names = pd.read_csv(os.path.join(DATAPATH, 'policynames.csv')).set_index('policy')

policies_drop = ['environment_preemption_naturalgasbans', 'w_environment_state_nepas_21', 'w_low_income_ee_21']
policies_subset = [p for p in sequence if p not in policies_drop]

colors = plt.cm.rainbow(np.linspace(0, 1, len(policies_subset)))

fig, ax = plt.subplots(figsize=(8, 22))

y = 0.
yticks = []
for i, policy in enumerate(policies_subset):

	if i > 0:
		y = y - 1. * np.max([len(s) for s in states_all])
	yticks.append(y)
	states_all = []
	for year in df['year'].unique():

		states = list(df.loc[(df['year'] == year) & (df[policy] == 1), 'stateabbr'].values)
		label = '\n'.join(states)
		ax.annotate(text=label, xy=(year, y), xycoords='data', ha='center', va='top', color=colors[i], fontsize=6)
		ax.plot(year, y, 'o', color='white')
		states_all.append(states)

#ax.set_ylim(-2, 11)
ax.set_yticks(yticks)
ax.set_yticklabels([df_names.loc[n, 'policy_long'] for n in policies_subset])
sns.despine(ax=ax, offset=1., right=True, top=True)
fig.savefig(os.path.join(FIGUREPATH, 'timeline.pdf'), bbox_inches='tight', transparent=True)
