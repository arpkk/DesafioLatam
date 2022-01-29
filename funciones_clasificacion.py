import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import funciones_clasificacion as fun
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import roc_auc_score


def concise_summary(mod, print_fit=True):
    #se guardan los parámetros asociados a estadísticas de ajuste
    fit = pd.DataFrame({'Statistics': mod.summary2().tables[0][2][2:],
    'Value': mod.summary2().tables[0][3][2:]})
    # se guardan los parámetros estimados por cada regresor.
    estimates = pd.DataFrame(mod.summary2().tables[1].loc[:, 'Coef.':
    'Std.Err.'])
    # imprimir fit es opcional
    if print_fit is True:
        print("\nGoodness of Fit statistics\n", fit)
        print("\nPoint Estimates\n\n", estimates)

def invlogit(x):
    return 1 / (1+np.exp(-x))

def analisis_modelo(x, y ,df):
    m1_ols = smf.ols(y+ "~"+ x, df).fit()
    concise_summary(m1_ols)
    sns.lmplot(x, y, df, line_kws={'color': 'tomato'}, scatter_kws={'color': 'grey', 'alpha': .5})
    m1_logit = smf.logit(y+ "~"+ x , df).fit()
    concise_summary(m1_logit)
    mean = df[x].mean()
    print("La media es de ", round(mean, 2))
    estimate_y = m1_logit.params['Intercept'] + (m1_logit.params[x]* mean)
    a= round(estimate_y, 2)
    print("El log odds estimado es de ",a)
    print("La probabilidad promedio de que el individuo percibe ingresos inferiores a 50.000 dólares anuales",round(fun.invlogit(estimate_y), 2))
    sns.lmplot(x, y, df,
               logistic=True,
               line_kws={'color': 'tomato', 'lw': 3},
               scatter_kws={'color': 'lightgrey', 'alpha': .5})
    decision_boundary = - m1_logit.params['Intercept'] / m1_logit.params[x]
    plt.axvline(decision_boundary, lw=1, color='dodgerblue')
    plt.axhline(.5, linestyle='--', color='grey', lw=1)
    plt.text(decision_boundary + .2, .5 + .05, r'Caso donde $\hat{p}=.5$',
             color='forestgreen')
    plt.plot(decision_boundary, .5, 'o', color='forestgreen')
    print("Una observación tiene igual probabilidad en ambos sucesos cuando x = ", round(decision_boundary, 3))

def learn(X_train, X_test, y_train, y_test, df):
    # Se estandariza la matriz de entrenamiento y de pruebas
    X_train_std = StandardScaler().fit_transform(X_train)

    X_test_std = StandardScaler().fit_transform(X_test)
    # Se el modelo con la clase LogisticRegression y se pasan los datos en fit.
    default_model = LogisticRegression().fit(X_train_std, y_train)
    yhat = default_model.predict(X_test_std)
    # Procede la matriz de confuncion para evaluar el desempeño
    m1_confusion = confusion_matrix(y_test, yhat)
    print("Matriz de confusion")
    print(m1_confusion)
    m1_acc = accuracy_score(y_test, yhat)
    print("Se calcula la exactitud promedio de datos que fueron correctamente predecidos: ",m1_acc)
    print("Se compara frente al caso de identificar aleatoriamente una observación correcta")
    print("Tiene un", m1_acc -.5 ,"superior que un clasificador aleatorio")
    m1_prec = precision_score(y_test, yhat)
    m1_rec = recall_score(y_test, yhat)
    m1_fscore = f1_score(y_test, yhat)
    print("Precision: ", m1_prec, "\nRecall: ", m1_rec, "\nF1: ", m1_fscore)
    print("Hay un ",m1_prec,"% de identificaciones positivas correctas. Hay un ",m1_rec,"% de positivos reales que se identificó correctamente. La medida general de desempeño es ",m1_fscore,"%.")

