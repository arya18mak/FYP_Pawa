import pandas as pd
import numpy as np


df1 = pd.read_csv("Sum of rainfall in each district.csv", index_col="Index")
data = np.random.randint(30, 100, size=len(df1))
df1["CN"] = data
print(df1)
