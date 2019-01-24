import pandas as pd
import numpy as np

df = pd.read_csv("temp.csv")
print(df)
print()

df = pd.read_csv("temp.csv", index_col=['S.No'])
print(df)
print()

df = pd.read_csv("temp.csv", dtype={'Salary': np.float64 })
print(df)
print()
print(df.dtypes)
print()

df = pd.read_csv("temp.csv", names=['a', 'b', 'c', 'd', 'e'])
print(df)
print()

df = pd.read_csv("temp.csv", names=['a', 'b', 'c', 'd', 'e'], header=0)
print(df)
print()

df = pd.read_csv("temp.csv", skiprows=2)
print(df)
print()