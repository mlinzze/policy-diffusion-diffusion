#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pandas as pd
import numpy as np

from statsmodels.stats.outliers_influence import variance_inflation_factor

from sklearn.linear_model import LogisticRegressionCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import PCA

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from sklearn.feature_selection import RFE
from sklearn.pipeline import Pipeline

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

## ============================================================

from parameters import *

## ============================================================

def select_variables_with_lasso(dataframe, variables, target_variable, cv_folds=10):
	"""
	Selects variables with the highest explanatory power using logistic regression with Lasso.

	Parameters:
	- dataframe (pd.DataFrame): The input data.
	- variables (list): List of candidate variable names to be considered in the model.
	- target_variable (str): The name of the target variable.
	- cv_folds (int): Number of folds for cross-validation.

	Returns:
	- list: Variable names with non-zero coefficients in the fitted model.
	"""
	# Extracting features and target from the dataframe
	X = dataframe[variables]
	y = dataframe[target_variable]

	# Standardize features and fit logistic regression with L1 penalty using cross-validation
	# to select the best regularization strength
	model = make_pipeline(StandardScaler(), LogisticRegressionCV(cv=cv_folds, penalty='l1', solver='saga', max_iter=10000))

	model.fit(X, y)

	# Extracting the model from the pipeline
	logistic_model = model.named_steps['logisticregressioncv']

	# Identifying variables with non-zero coefficients
	selected_variables = [var for var, coef in zip(variables, logistic_model.coef_.flatten()) if coef != 0]

	return selected_variables

def logistic_model_fit(dataframe, variables, target, use_cross_validation=False):
	"""
	Fits a logistic regression model using specified variables from the dataframe.

	Parameters:
	- dataframe (pd.DataFrame): The input data.
	- variables (list): List of variable names to be used in the model, excluding the target variable.
	- use_cross_validation (bool): If True, use 10-fold cross-validation to evaluate the model.
	  If False, use the accuracy score on the entire dataset.

	Returns:
	- float: The model fit measure (accuracy score).
	"""

	# Splitting features and target
	X = dataframe[variables]
	y = dataframe[target]

	model = LogisticRegression(max_iter=1000)

	if use_cross_validation:
		# Perform 10-fold cross-validation
		scores = cross_val_score(model, X, y, cv=10, scoring='accuracy')
		return scores.mean()
	else:
		# Fit the logistic regression model on the entire dataset
		model.fit(X, y)
		# Predict and calculate accuracy on the same dataset
		y_pred = model.predict(X)
		return accuracy_score(y, y_pred)

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

def vif(df, cols):
	X = df.loc[:, cols]
	vif_data = pd.DataFrame() 
	vif_data["feature"] = X.columns 
	vif_data["VIF"] = [variance_inflation_factor(X.values, i) 
						for i in range(len(X.columns))]
	return vif_data

def select_top_n_variables_with_pipeline(dataframe, target, n_variables, variables):
    X = dataframe[variables]
    y = dataframe[target]

    # Create a logistic regression model with L1 penalty
    logistic_model = LogisticRegression(penalty='l1', solver='saga', max_iter=10000, random_state=42)

    # Create a pipeline with standardization and logistic regression
    pipeline = Pipeline(steps=[
        ('scaler', StandardScaler()),
        ('logistic', logistic_model)
    ])

    # Initialize RFE with the logistic regression model, specifying the importance_getter for a pipeline
    rfe = RFE(estimator=pipeline, n_features_to_select=n_variables, step=1, importance_getter='named_steps.logistic.coef_')

    # Fit RFE
    rfe.fit(X, y)

    # Identify which variables were selected
    selected_variables = [var for var, selected in zip(variables, rfe.support_) if selected]

    return selected_variables

## ============================================================

df_policy = pd.read_csv(os.path.join(DATAPATH, 'data_policies.csv'))

# drop policy with first adoption in 2020! and less than 5 states
df_policy = df_policy.drop(columns=['environment_preemption_naturalgasbans'])
# drop policy with first adoption in 1974, and average adoption in 1974
df_policy = df_policy.drop(columns=['w_environment_state_nepas_21'])
# policy essentially only adopted in one year 2017
df_policy = df_policy.drop(columns=['w_low_income_ee_21'])

policies = df_policy.drop(columns=['state', 'year']).columns.values

df_expl = pd.read_csv(os.path.join(DATAPATH, 'data_merged_pca.csv'))

variables = ['log_gdppc', 'carbonintensity', 'democrat',
			'pctminingempl', 'pcttransutilempl', 'mininggdpshare', 'transutilgdpshare',
			'popdens', 'log_poptotal', 'log_area',
			'wind', 'solar', 'coal',
			'share_evangelical', 'climate_concern']

#df = df_expl.merge(df_policy, on=['state', 'year'], how='left')
df = df_expl.sort_values(by=['stateabbr', 'year'], ascending=True, ignore_index=True)
for policy in policies:
	df[policy] = df.groupby('stateabbr')[policy].transform(lambda x: (x.diff() > 0.).cumsum())

scaler = StandardScaler()
df.loc[:, variables] = scaler.fit_transform(df.loc[:, variables])

## ============================================================

pca_columns = ['PC{0:02d}'.format(i) for i in range(1, len(variables)+1, 1)]
pca = PCA().fit(df.loc[:, pca_columns])
explained_variance = np.cumsum(pca.explained_variance_ratio_)

CV = True

fit1_list = []
fit2_list = []
fit3_list = []
fit4_list = []
fit5_list = []
selected_variables_list = []
vif_list = []
for policy in policies:

	fit1 = logistic_model_fit(df, variables, policy, CV)
	variables_lasso = select_variables_with_lasso(df, variables, policy)
	if len(variables_lasso) > 0:
		fit2 = logistic_model_fit(df, variables_lasso, policy, CV)
	else:
		fit2 = np.nan

	fit3_list_n = []
	fit4_list_n = []
	fit5_list_n = []
	vif_list_n = []
	for n_components in range(1, len(variables)+1, 1):

		fit3 = logistic_model_fit(df, pca_columns[:n_components], policy, CV)
		fit3_list_n.append(fit3)

		selected_variables = select_top_n_variables_with_pipeline(df, policy, n_components, pca_columns)
		fit4 = logistic_model_fit(df, selected_variables, policy, CV)
		fit4_list_n.append(fit4)

		selected_variables = select_top_n_variables_with_pipeline(df, policy, n_components, variables)
		fit5 = logistic_model_fit(df, selected_variables, policy, CV)
		fit5_list_n.append(fit5)
		if n_components > 1:
			vif_list_n.append(vif(df, selected_variables)['VIF'].max())
		selected_variables_list.append(selected_variables)

	fit1_list.append(fit1)
	fit2_list.append(fit2)
	fit3_list.append(fit3_list_n)
	fit4_list.append(fit4_list_n)
	fit5_list.append(fit5_list_n)
	vif_list.append(vif_list_n)

fit3_list_cond = []
fit4_list_cond = []
fit5_list_cond = []
vif_list_cond = []
for n_components in range(1, len(variables)+1, 1):
	
	fit3_list_cond.append(np.mean([x[n_components-1] for x in fit3_list])) 
	fit4_list_cond.append(np.mean([x[n_components-1] for x in fit4_list])) 
	fit5_list_cond.append(np.mean([x[n_components-1] for x in fit5_list]))
	try:
		vif_list_cond.append(np.mean([x[n_components-1] for x in vif_list])) 
	except:
		pass

fit1 = np.mean(fit1_list)
fit2 = np.nanmean(fit2_list)

print(fit1)
print(fit2)
print(fit3_list_cond)
print(fit4_list_cond)
print(fit5_list_cond)

selected_variables_list_flat = [item for sublist in selected_variables_list for item in sublist]
print(pd.value_counts(selected_variables_list_flat))

lags = [c for c in df.columns if c.split('_')[-1] == 'sld']
df.loc[:, variables + lags].corr().loc[lags, variables].max(axis=1).mean(axis=0)
df.loc[:, pca_columns + lags].corr().loc[lags, pca_columns].max(axis=1).mean(axis=0)

vif1_list = []
vif2_list = []
for i, lag in enumerate(lags):
	vif1 = vif(df.loc[:, variables + lags], variables[:4] + [lag])
	vif2 = vif(df.loc[:, pca_columns + lags], pca_columns[:4] + [lag])
	vif1_list.append(vif1.loc[vif1['feature'] == lag, 'VIF'].values[0])
	vif2_list.append(vif2.loc[vif2['feature'] == lag, 'VIF'].values[0])

fig, ax = plt.subplots()
ax.plot([1., len(variables)], [fit1, fit1], 'k-', label='All 15 variables')
ax.plot([1., len(variables)], [fit2, fit2], 'b-', label='Lasso with 10-fold CV')
ax.plot(np.arange(1., len(variables)+1, 1), fit3_list_cond, 'r-', label=r'First $n$ principal components')
ax.plot(np.arange(1., len(variables)+1, 1), fit4_list_cond, 'm-', label=r'Best $n$ principal components')
ax.plot(np.arange(1., len(variables)+1, 1), fit5_list_cond, 'g-', label=r'Best $n$ variables')
ax.set_xlabel(r'Number of variables $n$')
ax.set_ylabel('Explanatory power of model')
ax.set_ylim(0.8, 0.89)
ax.set_xticks(np.arange(1, 15+1, 1))
ax2 = ax.twinx()
ax2.plot(np.arange(1., len(variables)+1, 1), explained_variance, 'y-', label=r'Explained variation of first $n$ principal components')
ax2.set_ylabel('Explained variation of principal components')
ax.legend(loc='upper left', title='Left axis', alignment='left', bbox_to_anchor=(1.15, 1.05))
ax2.legend(loc='upper left', title='Right axis', alignment='left', bbox_to_anchor=(1.15, 0.65))
ax2.set_ylim(0.2, 1.)
sns.despine(ax=ax, offset=1., right=True, top=True, left=False)
sns.despine(ax=ax2, offset=1., right=False, top=True, left=True)
fig.savefig(os.path.join(FIGUREPATH, 'explained_variation.pdf'), bbox_inches='tight', transparent=True)

