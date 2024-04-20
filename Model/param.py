import numpy as np 
import pandas as pd
from time_risk import trr
from pathlib import Path

def get_params(dataframe):
    df2019= pd.read_csv('Downloads/accidents_Berlin_2019.csv',sep=";",encoding='latin1')
    df2021 = pd.read_csv('Downloads/accidents_Berlin_2021.csv',sep = ';',encoding='latin1')
    df = pd.concat([df2019, df2021])
    print("Data collected")
    selected_columns = ['UWOCHENTAG', 'USTUNDE', 'ULICHTVERH','USTRZUSTAND']  # Replace with the actual column names you want to extract
    df_refined = dataframe[selected_columns]
    #print(df_refined.head(10))
    time_columns = ['UWOCHENTAG', 'USTUNDE']
    time = df_refined[time_columns]
    time_related_risk = trr(time)
    #print(time_related_risk)
    df_refined['Time Related Risk'] = time_related_risk['Risk']
    #with open(Path())
    #df_refined.to_csv('Downloads/accidents_Berlin_2019_refined.csv', sep=';', index=False)
    #return 

