#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 23:50:39 2019

@author: swuser
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, RidgeCV,LassoCV
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

train = pd.read_csv("2016_properties_60000v3_train.csv").dropna()
test = pd.read_csv("2016_properties_60000v3_test.csv").dropna()

train_y = train.iloc[:,7]
test_y = test.iloc[:,7]
train_xs = train.iloc[:,1:15].drop(["taxvaluedollarcnt"],axis=1)
test_xs = test.iloc[:,1:15].drop(["taxvaluedollarcnt"],axis=1)

train_xl = train.drop(["parcelid","taxvaluedollarcnt"],axis=1)
test_xl = test.drop(["parcelid","taxvaluedollarcnt"],axis=1)

score = []
error = []
# linear regression
lin = LinearRegression(n_jobs=-1).fit(train_xs,train_y)
test_ys_pred1 = lin.predict(test_xs)
score.append(lin.score(test_xs,test_y))
error.append(mean_squared_error(test_y,test_ys_pred1))
lin = LinearRegression(n_jobs=-1).fit(train_xl,train_y)
test_yl_pred1 = lin.predict(test_xl)
score.append(lin.score(test_xl,test_y))
error.append(mean_squared_error(test_y,test_yl_pred1))

#  Ridge
ridge = RidgeCV(cv=5).fit(train_xs,train_y)
score.append(ridge.score(test_xs,test_y))
test_ys_pred2 = ridge.predict(test_xs)
error.append(mean_squared_error(test_y,test_ys_pred2))

ridge = RidgeCV(cv=5).fit(train_xl,train_y)
score.append(ridge.score(test_xl,test_y))
test_yl_pred2 = ridge.predict(test_xl)
error.append(mean_squared_error(test_y,test_yl_pred2))

# Lasso
lasso = LassoCV(cv=5).fit(train_xs,train_y)
score.append(lasso.score(test_xs,test_y))
test_ys_pred3 = lasso.predict(test_xs)
error.append(mean_squared_error(test_y,test_ys_pred3))


lasso = LassoCV(cv=5).fit(train_xl,train_y)
score.append(lasso.score(test_xl,test_y))
test_yl_pred3 = lasso.predict(test_xl)
error.append(mean_squared_error(test_y,test_yl_pred3))

# SVR
scaler = StandardScaler()
scaler.fit(train_xs)
train_xs_std = scaler.transform(train_xs)
test_xs_std = scaler.transform(test_xs)
scaler.fit(train_xl)
train_xl_std = scaler.transform(train_xl)
test_xl_std = scaler.transform(test_xl)

svrrbf = GridSearchCV(SVR(kernel='rbf'),cv=5,param_grid={"C":[0.1,1,10,100],
                      "gamma":[0.1,0.5,1,5,10]},n_jobs=-1)
svrrbf.fit(train_xs,train_y)
score.append(svrrbf.score(test_xs,test_y))
test_ys_pred = svrrbf.predict(test_xs)
error.append(mean_squared_error(test_y,test_ys_pred))
#SVR(C=100, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma=0.1,
  #kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)
svrrbf = GridSearchCV(SVR(kernel='rbf'),cv=5,param_grid={"C":[0.1,1,10,100],
                      "gamma":[0.1,0.5,1,5,10]},n_jobs=-1)
svrrbf.fit(train_xs_std,train_y)
score.append(svrrbf.score(test_xs_std,test_y))
test_ys_pred = svrrbf.predict(test_xs_std)
error.append(mean_squared_error(test_y,test_ys_pred))


svrrbf = GridSearchCV(SVR(kernel='rbf'),cv=5,param_grid={"C":[0.1,1,10,100],
                      "gamma":[0.1,0.5,1,5,10]},n_jobs=-1)
svrrbf.fit(train_xl_std,train_y)
score.append(svrrbf.score(test_xl_std,test_y))
test_yl_pred = svrrbf.predict(test_xl_std)
error.append(mean_squared_error(test_y,test_yl_pred))
#SVR(C=100, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma=0.1,
 # kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)
# SVR linear
svrrbf = GridSearchCV(SVR(kernel='linear'),cv=5,param_grid={"C":[0.1,1,10,100]},n_jobs=-1)
svrrbf.fit(train_xs_std,train_y)
score.append(svrrbf.score(test_xs_std,test_y))
test_ys_pred = svrrbf.predict(test_xs_std)
error.append(mean_squared_error(test_y,test_ys_pred))
#C=100

svrrbf = GridSearchCV(SVR(kernel='linear'),cv=5,param_grid={"C":[0.1,1,10,100]},n_jobs=-1)
svrrbf.fit(train_xl_std,train_y)
score.append(svrrbf.score(test_xl_std,test_y))
test_yl_pred = svrrbf.predict(test_xl_std)
error.append(mean_squared_error(test_y,test_yl_pred))
#C=100

# SVR ori
svrrbf = GridSearchCV(SVR(kernel='linear'),cv=5,param_grid={"C":[0.1,1,10,100]},n_jobs=-1)
svrrbf.fit(train_xs,train_y)
score.append(svrrbf.score(test_xs,test_y))
test_ys_pred = svrrbf.predict(test_xs)
error.append(mean_squared_error(test_y,test_ys_pred))
#C=100

svrrbf = GridSearchCV(SVR(kernel='linear'),cv=5,param_grid={"C":[0.1,1,10,100]},n_jobs=-1)
svrrbf.fit(train_xl,train_y)
score.append(svrrbf.score(test_xl,test_y))
test_yl_pred = svrrbf.predict(test_xl)
error.append(mean_squared_error(test_y,test_yl_pred))
#C=100

# random forest score at 7 and 8
rfc_best=RandomForestRegressor(max_depth=10,max_features='log2',min_samples_split= 0.05,n_estimators= 100, n_jobs = -1)
rf_result_best=rfc_best.fit(train_xs, train_y)
test_ys_pred6=rf_result_best.predict(test_xs)
score.append(rfc_best.score(test_xs,test_y))
error.append(mean_squared_error(test_y,test_ys_pred6))

feat_imports=pd.Series(rf_result_best.feature_importances_, index=train_xs.columns.tolist())
feat_imports_10=feat_imports.sort_values(ascending=False)[:10]
feat_imports_10.plot(kind='bar')
plt.show()

rfc_bestl=RandomForestRegressor(max_depth=10,max_features='log2',min_samples_split= 0.05,n_estimators= 100, n_jobs = -1)
rf_result_bestl=rfc_bestl.fit(train_xl, train_y)
test_yl_pred6=rf_result_bestl.predict(test_xl)
score.append(rfc_bestl.score(test_xl,test_y))
error.append(mean_squared_error(test_y,test_yl_pred6))


feat_importl=pd.Series(rf_result_bestl.feature_importances_, index=train_xl.columns.tolist())
feat_importl_10=feat_importl.sort_values(ascending=False)[:10]
feat_importl_10.plot(kind='bar')
plt.show()

# ensemble
test_ys_pred = (test_ys_pred1+test_ys_pred2+test_ys_pred3+test_ys_pred6)/4
test_yl_pred = (test_yl_pred1+test_yl_pred2+test_yl_pred3+test_yl_pred6)/4
error.append(mean_squared_error(test_y,test_ys_pred))
error.append(mean_squared_error(test_y,test_yl_pred))
train_yl_pred1 = ridge.predict(train_xl)
np.savetxt("train_y_pred.txt",train_yl_pred1)
np.savetxt("test_y_pred.txt",test_yl_pred1)

train["pred"]=train_yl_pred1
test["pred"]=test_yl_pred1
train.to_csv("train_v4.csv")
test.to_csv("test_v4.csv")