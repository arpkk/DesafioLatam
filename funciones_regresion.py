import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
import funciones_regresion as fun
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def analisis_modelo(x,y,df):
    m1_ols = smf.ols(y+ "~"+x, data=df).fit()
    print(m1_ols.summary())
    sns.regplot(df[x], df[y], order=2, line_kws={'color': 'tomato'})

def ref(df, y_vec, X_mat):
    X_train, X_test, y_train, y_test =train_test_split(X_mat, y_vec,test_size=.33, random_state=11238)
    model=linear_model.LinearRegression(fit_intercept=True,normalize=True)
    model.fit(X_train, y_train)
    model_yhat=model.predict(X_test)
    report_scores(model_yhat,y_test)


def report_scores(pre, val):
    print('Error cuadratico=', mean_squared_error(val, pre))
    print('r2=', r2_score(val, pre))