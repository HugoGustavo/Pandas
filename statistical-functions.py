import pandas as pd
import numpy as np

series = pd.Series([1, 2, 3, 4, 5])
print(series.pct_change())
print()

df = pd.DataFrame(np.random.randn(5,2))
print(df.pct_change())
print()

series1 = pd.Series(np.random.randn(10))
series2 = pd.Series(np.random.randn(10))
print(series1.cov(series2))
print()

frame = pd.DataFrame(np.random.randn(10,5), columns=['a', 'b', 'c', 'd', 'e'])
print(frame['a'].cov(frame['b']))
print()
print(frame.cov())
print()

frame = pd.DataFrame(np.random.randn(10,5), columns=['a', 'b', 'c', 'd', 'e'])
print(frame['a'].corr(frame['b']))
print()
print(frame.corr())
print()

series = pd.Series(np.random.randn(5), index=list('abcde'))
series['d'] = series['b']
print(series.rank())
print()