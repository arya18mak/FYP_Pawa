import pandas as pd
import numpy as np

df1 = pd.read_csv("cn.csv")
df1['suitability'] = 'low'
sta_array = df1['State'].unique()
print(df1)
df2 = pd.DataFrame()
for state in sta_array:
    f = df1.loc[df1['State'] == state]
    f['suitability'] = 'moderate'
    x = np.array(f['Runoff'])
    one_fourth = np.percentile(x, 25)
    three_fourth = np.percentile(x, 75)
    l = len(f['State'])
    """for i in range(0, l - 1):
        if f[i]['Total_rainfall'] < one_fourth:
            f[i]['suitability'] = 'low'

        elif one_fourth < f[i]['Total_rainfall'] < three_fourth:
            f[i]['suitability'] = 'moderate'

        else:
            f[i]['suitability'] = 'high'"""
    f.loc[f['Runoff'] < one_fourth, 'suitability'] = 'low'
    f.loc[(f['Runoff'] < three_fourth) & (f['Runoff'] > one_fourth), 'suitability'] = 'moderate'
    f.loc[f['Runoff'] > three_fourth, 'suitability'] = 'high'
    if state == sta_array[0]:
        df2 = f.copy()
    else:
        df2 = df2.append(f)

print(df2)
df2.to_csv("Classified_output_acctoquartile_runoff.csv")
