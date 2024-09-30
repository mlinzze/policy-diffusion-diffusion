#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from copy import deepcopy

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns


## ============================================================

from parameters import *

## ============================================================

variable2name = {
	'log_gdppc': 'log GDP pc',
	'carbonintensity': 'GHG intensity',
	'democrat': 'Democratic control',
	'pctminingempl': 'Employment in mining',
	'pcttransutilempl': 'Employment in transport and utilities',
	'mininggdpshare': 'GDP of mining',
	'transutilgdpshare': 'GDP of transport and utilities',
	'popdens': 'Population density',
	'log_poptotal': 'log Population',
	'log_area': 'log Land area',
	'wind': 'Wind power potential',
	'solar': 'Solar power potential',
	'coal': 'Coal production',
	'share_evangelical': 'Share evangelical',
	'climate_concern': 'Concern about climate change'
}

variable2unit = {
	'log_gdppc': 'USD per capita',
	'carbonintensity': 't CO2eq per USD',
	'democrat': 'Binary',
	'pctminingempl': 'Percent',
	'pcttransutilempl': 'Percent',
	'mininggdpshare': 'Percent',
	'transutilgdpshare': 'Percent',
	'popdens': 'People per km2',
	'log_poptotal': 'People',
	'log_area': 'km2',
	'wind': 'm/s', # Wind speed in 
	'solar': 'kWh per m2 per day', # Global horizontal solar irradiance in 
	'coal': 'Binary',
	'share_evangelical': 'Percent',
	'climate_concern': 'Score'
}

variable2source = {
	'log_gdppc': 'MISS',
	'carbonintensity': 'MISS',
	'democrat': 'MISS',
	'pctminingempl': 'MISS',
	'pcttransutilempl': 'MISS',
	'mininggdpshare': 'MISS',
	'transutilgdpshare': 'MISS',
	'log_poptotal': 'U.S. Census Bureau',
	'popdens': 'U.S. Census Bureau',
	'log_area': 'U.S. Census Bureau',
	'wind': 'U.S. Department of Energy (NREL)',
	'solar': 'U.S. Department of Energy (NREL)',
	'coal': 'U.S. Energy Information Administration',
	'share_evangelical': '\\citet{sellers2017}',
	'climate_concern': '\citet{bergquist2019}',
}

policy2name = pd.read_csv(os.path.join(DATAPATH, 'policygroups.csv'), sep=';').loc[:, ['Policy short', 'Policy long']]
policy2name = dict(zip(policy2name.iloc[:, 0], policy2name.iloc[:, 1]))

## ============================================================

variables = ['log_gdppc', 'carbonintensity', 'democrat',
			'pctminingempl', 'pcttransutilempl', 'mininggdpshare', 'transutilgdpshare',
			'popdens', 'log_poptotal', 'log_area',
			'wind', 'solar', 'coal',
			'share_evangelical', 'climate_concern']

## ============================================================

df_sources = pd.DataFrame({'Variable': variables})
df_sources['Source'] = df_sources['Variable'].apply(lambda x: variable2source.get(x, x))
df_sources['Variable'] = df_sources['Variable'].apply(lambda x: variable2name.get(x, x).replace('_', ' '))

tablefile = 'table_sources.tex'
df_sources.to_latex(buf=os.path.join(TABLEPATH, tablefile), index=False, encoding='utf-8',
		float_format="%.2f", escape=False, column_format='l'+'l'*(df_sources.shape[1]-1) + 'l', na_rep='')

## ============================================================

df = pd.read_csv(os.path.join(DATAPATH, 'data_merged.csv'))
df = df.sort_values(by=['state', 'year'], ascending=True, ignore_index=True)

df['share_evangelical'] = df['share_evangelical'] * 100.

df_desc = pd.DataFrame({'Variable': variables})
df_desc['Unit'] = df_desc['Variable'].apply(lambda x: variable2unit.get(x, x))
df_desc['Mean'] = df_desc['Variable'].apply(lambda x: df[x].mean())
df_desc['Sd'] = df_desc['Variable'].apply(lambda x: df[x].std())
df_desc['Min'] = df_desc['Variable'].apply(lambda x: df[x].min())
df_desc['Max'] = df_desc['Variable'].apply(lambda x: df[x].max())
df_desc['Variable'] = df_desc['Variable'].apply(lambda x: variable2name.get(x, x).replace('_', ' '))
df_desc.columns = [c.replace('_', ' ') for c in df_desc.columns]

tablefile = 'table_descriptives.tex'
df_desc.to_latex(buf=os.path.join(TABLEPATH, tablefile), index=False, encoding='utf-8',
		float_format="%.2f", escape=False, column_format='l'+'r'*(df_desc.shape[1]-1) + 'l', na_rep='')

## ============================================================

policies_drop = ['environment_preemption_naturalgasbans', 'w_environment_state_nepas_21', 'w_low_income_ee_21']
df_policies = pd.read_csv(os.path.join(DATAPATH, 'policygroups.csv'), sep=';')
df_policies = df_policies.loc[df_policies['Binary coding'] == 1, :].loc[:, ['Policy short', 'Policy long', 'Categories C']]
df_policies = df_policies.loc[~df_policies['Policy short'].isin(policies_drop), :]

df_policy = pd.read_csv(os.path.join(DATAPATH, 'data_policies.csv'))
df_policy = df_policy.drop(columns=['year']).groupby('state').max().sum().T.reset_index().rename(columns={'index': 'Policy short', 0: 'Count'})

df_policies = df_policies.merge(df_policy, on='Policy short').drop(columns='Policy short')
df_policies = df_policies.rename(columns={'Policy long': 'Policy', 'Categories C': 'Instrument type'})

tablefile = 'table_policies.tex'
df_policies.to_latex(buf=os.path.join(TABLEPATH, tablefile), index=False, encoding='utf-8',
		float_format="%.2f", escape=False, column_format='ll'+'r'*(df_policies.shape[1]-2), na_rep='')

## ===================

df_xy = df_policies.groupby('Instrument type')['Policy'].count()
x = df_xy.values
y = np.arange(0., np.size(x), 1.)
ylabels = df_xy.index.values

fig, ax = plt.subplots()
ax.barh(y=y, width=x, height=0.8, align='center')
ax.set_yticks(y)
ax.set_yticklabels(ylabels)
ax.set_xlabel('Number of policies')
ax.set_ylabel('Instrument type')
#ax.set_ylim(0.8, 0.9)
#ax.set_xticks(np.arange(1, 15+1, 1))
#ax.legend(loc='upper left', title='Left axis', alignment='left')
sns.despine(ax=ax, offset=1., right=True, top=True, left=False)
fig.savefig(os.path.join(FIGUREPATH, 'policies_counts.pdf'), bbox_inches='tight', transparent=True)

