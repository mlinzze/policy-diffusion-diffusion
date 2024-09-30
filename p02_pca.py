#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import copy
import itertools
import random

import numpy as np
import pandas as pd

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

## ============================================================

from parameters import *

## ============================================================

def pca_convenient(df, cols, n_components):
	scaler = StandardScaler()
	pca = PCA(n_components=n_components)
	pipeline = make_pipeline(scaler, pca)
	principalComponents = pipeline.fit_transform(df[cols])
	pca_columns = ['PC{0:02d}'.format(i) for i in range(1, n_components+1, 1)]
	pca_df = pd.DataFrame(data=principalComponents, columns=pca_columns)
	df = pd.concat([df, pca_df], axis=1)
	return df

def expand_df(df, dims, values):
	df = df.set_index(dims)
	multi_index = (pd.MultiIndex.from_product(
			iterables=values,
			names=dims))
	df = df.reindex(multi_index, fill_value=np.nan).reset_index()
	df = df.sort_values(by=dims, ascending=True).reset_index(drop=True)
	return df

## ============================================================

df = pd.read_csv(os.path.join(DATAPATH, 'data_merged.csv'))
df = df.sort_values(by=['stateabbr', 'year'], ascending=True, ignore_index=True)
df['year'] = df['year'].astype(int)

states = list(df['stateabbr'].unique())
years = list(range(1980, 2020+1, 1))
df = df.loc[df['year'].isin(years), :]
df = expand_df(df, ['stateabbr', 'year'], [states, years])

## ============================================================

variables_pca = ['log_gdppc', 'carbonintensity', 'democrat',
					'pctminingempl', 'pcttransutilempl', 'mininggdpshare', 'transutilgdpshare',
					'popdens', 'log_poptotal', 'log_area',
					'wind', 'solar', 'coal',
					'share_evangelical', 'climate_concern']

df = pca_convenient(df, variables_pca, len(variables_pca))

## ============================================================

df.to_csv(os.path.join(DATAPATH, 'data_merged_pca.csv'), index=False)


