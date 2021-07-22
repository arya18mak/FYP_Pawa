import pandas as pd
import numpy as np

df1 = pd.read_csv("prediction_using_ 4_optimizers.csv")
df1 = df1.drop(['RMSE', 'Optimizer'], axis=1)
sta_array = df1['State'].unique()
dis_array = df1['District'].unique()
print(sta_array)
print(dis_array)
df2 = pd.DataFrame(columns=['State', 'District', 'Total_rainfall'])

for state in sta_array:
    f = df1.loc[df1['State'] == state]
    dis_unique = f['District'].unique()
    for district in dis_unique:
        main_column = df1['2021'].loc[df1['District'] == district]
        y = main_column.sum()
        df2.loc[len(df2.index)] = [state, district, y]


df2.to_csv("Sum of rainfall in each district.csv")
