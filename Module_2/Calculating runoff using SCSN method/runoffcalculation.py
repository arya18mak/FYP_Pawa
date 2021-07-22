import pandas as pd
import numpy as np
import random

df1 = pd.read_csv("cn.csv")
df1['S'] = df1.apply(lambda row: (1000/row.CN)-10, axis=1)
df1['runoff'] = df1.apply(lambda row: ((row.Total_rainfall - 0.2*row.S)**2)/(row.Total_rainfall + 0.8*row.S), axis=1)
print(df1)
df1.to_csv("cn.csv")
