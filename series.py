import pandas as pd
import numpy as np

s = pd.Series()
print(s)

data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
print(s)

data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data, index=[100,101,102,103])
print(s)

data = {'a':0., 'b':1., 'c':2.}
s = pd.Series(data)
print(s)

data = {'a': 0., 'b':1., 'c':2.}
s = pd.Series(data, index=['b', 'c', 'd', 'a'])
print(s)

s = pd.Series(5, index=[0,1,2,3])
print(s)

s = pd.Series([1,2,3,4,5], index=['a', 'b', 'c', 'd', 'e'])
print(s[0])

s = pd.Series([1,2,3,4,5], index=['a', 'b', 'c', 'd', 'e'])
print(s[:3])

s = pd.Series([1,2,3,4,5], index=['a', 'b', 'c', 'd', 'e'])
print(s[-3:])

s = pd.Series([1,2,3,4,5], index=['a', 'b', 'c', 'd', 'e'])
print(s['a'])

s = pd.Series([1,2,3,4,5], index=['a', 'b', 'c', 'd', 'e'])
print(s[['a', 'c', 'd']])

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
# print(s['f'])