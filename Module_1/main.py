import pandas as pd
import tensorflow as tf
import numpy as np

import matplotlib.pyplot as plt

df1 = pd.read_csv('Average temperature_1901-2002.csv')
df2 = pd.read_csv('Precipitation_1901-2002.csv')
df3 = pd.read_csv('Vapour pressure_1901-2002.csv')
df4 = pd.read_csv('Cloud cover_1901-2002.csv')
df5 = pd.read_csv('Maximum temperature_1901-2002.csv')
df6 = pd.read_csv('Minimum temperature_1901-2002.csv')
df_avg = pd.read_csv('avg_temp_predictions.csv')
df_vap = pd.read_csv('vapour_pressure_predictions.csv')
df_cc = pd.read_csv('cloud_cover_predictions.csv')
df_max = pd.read_csv('max_temp_predictions.csv')
df_min = pd.read_csv('minimum_temp_predictions.csv')
av_array = df1['District'].unique()
pre_array = df2['District'].unique()
vap_array = df3['District'].unique()
cc_array = df4['District'].unique()
max_array = df5['District'].unique()
min_array = df6['District'].unique()
av_array_as_set = set(av_array)
pre_array_as_set = set(pre_array)
vap_array_as_set = set(vap_array)
cc_array_as_set = set(cc_array)
max_array_as_set = set(max_array)
min_array_as_set = set(min_array)
intersection_as_list = list(av_array_as_set & pre_array_as_set & cc_array_as_set & vap_array_as_set & max_array_as_set &
                            min_array_as_set)
print(intersection_as_list)
dis_arr = np.array(intersection_as_list)
print(dis_arr)
print(len(dis_arr))
dis_arr1 = dis_arr
finale = pd.DataFrame()
for dist in dis_arr1:
    f = df1.loc[df1['District'] == dist]
    sing = np.array(f["State"].unique())
    g = df2.loc[df2['District'] == dist]
    h = df3.loc[df3['District'] == dist]
    z = df4.loc[df4['District'] == dist]
    t = df5.loc[df5['District'] == dist]
    n = df6.loc[df6['District'] == dist]
    arr = np.array(df1.columns)
    col_list = arr[3:]
    callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3)
    prediction_year1 = []
    prediction_year2 = []
    #prediction = []
    rm_se = np.empty(shape=0)
    a = 0
    pre_columns = np.array(df_avg.columns)
    qwert = pre_columns[-2:]
    for x in col_list:
        xyz = f[x].to_numpy()
        uvw = g[x].to_numpy()
        rst = h[x].to_numpy()
        opq = z[x].to_numpy()
        fgh = t[x].to_numpy()
        bnm = n[x].to_numpy()
        new_avg = np.divide(xyz, np.amax(xyz))
        new_vap = np.divide(rst, np.amax(rst))
        new_pre = np.divide(uvw, np.amax(uvw))
        new_cc = np.divide(opq, np.amax(opq))
        new_max = np.divide(fgh, np.max(fgh))
        new_min = np.divide(bnm, np.amax(bnm))
        ys = new_pre
        list2 = []
        for i in range(102):
            list1 = [new_avg[i], new_vap[i], new_cc[i], new_max[i], new_min[i]]
            list2.append(list1)

        combined_array = np.array(list2)
        print(combined_array)
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(units=5, input_shape=[5]),
            tf.keras.layers.Dense(3),
            tf.keras.layers.Dense(2),
            tf.keras.layers.Dense(1)

        ])

        model.compile(optimizer='Nadam', loss='mean_squared_error')
        history = model.fit(combined_array, ys, epochs=500, callbacks=callback)
        e = history.history['loss'][-1]
        rm_se = np.append(rm_se, e)
        """       predictions = np.amax(uvw)*model.predict(combined_array)[u-1901]
        fil_predictions = np.maximum(predictions, 0)
        prediction.append(fil_predictions)
        print(fil_predictions)
        prediction = np.array(prediction)
        print(prediction)"""

        for year in qwert:
            q = df_avg[year]
            j = df_vap[year]
            w = df_max[year]
            e = df_cc[year]
            o = df_min[year]
            lst2 = []
            lst1 = [q[a] / np.amax(xyz), j[a] / np.amax(rst), e[a] / np.amax(opq), w[a] / np.amax(fgh),
                    o[a] / np.amax(bnm)]
            lst2.append(lst1)
            comb_arr = np.array(lst2)
            print(np.amax(uvw) * model.predict(comb_arr))
            if year == '2021':
                arr1 = np.amax(uvw) * model.predict(comb_arr)[0]
                print(prediction_year1.append(arr1[0]))
            else:
                arr2 = np.amax(uvw) * model.predict(comb_arr)[0]
                prediction_year2.append(arr2[0])
        a = a + 1
        print(a)
    year_2021 = np.absolute(prediction_year1)#np.maximum(prediction_year1, 0)
    year_2022 = np.absolute(prediction_year2)#np.maximum(prediction_year2, 0)
    asd = np.vstack((year_2021, year_2022)).T
    print(prediction_year1)
    print(prediction_year2)
    r = pd.DataFrame(asd, columns=qwert)
    r.insert(0, 'State', sing[0])
    r.insert(1, 'District', dist)
    r.insert(2, 'Month', col_list)
    r.insert(5, 'RMSE', rm_se)
    print(r)
    if dist == dis_arr[0]:
        finale = r.copy()
    else:
        finale = finale.append(r)

finale2 = finale.sort_values(by=['State', 'District'], ascending=True)
finale2.to_csv('rainfall_prediction_Nadam.csv', index=False)
