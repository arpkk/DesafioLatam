import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def med_desp(df):
    print("Frecuencia de: ",df.groupby("ht_region").size())
    print("Media de undp_hdi: ", df["undp_hdi"].mean(), "variabilidad: ", df["undp_hdi"].var())
    print("Media de gle_cgdpc: ", df["gle_cgdpc"].mean(), "variabilidad: ", df["gle_cgdpc"].var())
    print("Media de imf_pop: ", df["imf_pop"].mean(), "variabilidad: ", df["imf_pop"].var())
    print("Media de wef_imort: ", df["wef_imort"].mean(), "variabilidad: ", df["wef_imort"].var())
    print("Media de who_alc2000: ", df["who_alc2000"].mean(), "variabilidad: ", df["who_alc2000"].var())
    print("Media de who_tobt: ", df["who_tobt"].mean(), "variabilidad: ", df["who_tobt"].var())
    print("Media de wdi_exph: ", df["wdi_exph"].mean(), "variabilidad: ", df["wdi_exph"].var())

def perdida(dataframe, var, print_list=False):
    cant= dataframe[var].isna().sum()
    porcen= str(cant*100/len(dataframe))+"%"
    if print_list:
        print(var)
        print(dataframe[var].describe())
        print("Porcentaje de perdidas de",var,": ",porcen)
    return [cant, porcen]

def graficar_media(sample_df, full_df ,var ,sample_mean=False, true_mean=True):
    datavar=sample_df[var].dropna()
    datapobl=full_df[var].dropna()
    plt.hist(datavar)
    if sample_mean:
        plt.axvline(datavar.mean(), lw=3, color="tomato", linestyle="--")
    if true_mean:
        plt.axvline(datapobl.mean(), lw=3, color="blue", linestyle="--")

def dotplot(dataframe,plot_var,plot_by,statistic="mean",global_stat=False):
    data=dataframe.groupby(plot_by)[plot_var]
    if statistic=="mean":
        data_values=data.mean()
    if statistic=="median":
        data_values=data.median()
    plt.plot(data_values.values, data_values.index, "o")
    if global_stat==True:
        if statistic=="mean":
            plt.axvline(dataframe[plot_var].mean(), lw=3, color="tomato", linestyle="--")
        if statistic=="median":
            plt.axvline(dataframe[plot_var].median(), lw=3, color="tomato", linestyle="--")