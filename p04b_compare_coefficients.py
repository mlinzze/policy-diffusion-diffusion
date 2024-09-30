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

linsenmeier_ncc = [0.9152, 0.2251] # these are betas
#raghoo_2022 = [4.709, 1.062] # Table 4, Model 1 - Note issue of multicollinearity, several lags https://www.sciencedirect.com/science/article/pii/S0959652622019333#appsec1
raghoo_2022 = [2.270, 0.563] # Table 8, Model 1 - EHA here uses also Cox, see methods section
abel_2019 = [1.528, 0.732] # Table 2, Column 1
#sauquet_2014 = np.log([0.996, 0.010]) # Table 2, Column 1: these are hazard ratios; negative effects; but difficult to understand because multiple lags included
bromley_2016 = [1.621, 0.217] # Table 2, Column 1; it seems that these are betas
linsenmeier_states = [1.95, 0.46]

## ============================== ##

studies = [linsenmeier_ncc,
			raghoo_2022,
			abel_2019,
			bromley_2016,
			linsenmeier_states]
labels = ['Linsenmeier et al. 2023\n(carbon pricing internationally)',
		'Raghoo & Shah 2022\n(carbon pricing internationally)',
		'Abel 2019\n(climate policies in Germany)',
		'Bromley & Trujillo 2017\n(climate policies in the USA)',
		'This study\n(climate policies in the USA)']

fig, ax = plt.subplots(figsize=(5,5))
for i, study in enumerate(studies):
	ax.errorbar(study[0], i, xerr=study[1] * 1.96, color='grey', lw=3.)
	ax.plot(study[0], i, 'ko', markersize=8)
	ax.annotate(labels[i] + '\n', xy=(study[0], i), xycoords='data', ha='center', va='bottom')
#ax.legend()
ax.set_yticks(range(len(studies)))
ax.set_yticklabels([])
ax.plot([0., 0.], [-1., len(studies)+1], 'k--')
ax.set_ylim(-1., len(studies))
ax.set_xlim(-1.4, 4.5)
ax.set_xlabel('Estimated coefficient of spatial lag')
#ax.set_ylabel('Article')
sns.despine(ax=ax, offset=1., right=True, top=True)
fig.savefig(os.path.join(FIGUREPATH, 'coefficients_comparison.pdf'), bbox_inches='tight', dpi=300., transparent=True)
