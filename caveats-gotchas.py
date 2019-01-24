import pandas as pd
import numpy as np

if ( pd.Series([False, True, False]).any()):
    print('I am True')
    print()

print(pd.Series([True]).bool())
print()

series = pd.Series(range(5))
print(series == 4)
print()

series = pd.Series(list('abc'))
series = series.isin(['a', 'c', 'e'])
print(series)
print()

df = pd.DataFrame(np.random.randn(6,4), columns=['one', 'two', 'three', 'four'], index=list('abcdef'))
print(df)
print()
print(df.ix[['b', 'c', 'e']])
print()

df = pd.DataFrame(np.random.randn(6,4), columns=['one', 'two', 'three', 'four'], index=list('abcdef'))
print(df)
print()
print(df.reindex(['b', 'c', 'e']))
print()

df = pd.DataFrame(np.random.randn(6,4), columns=['one', 'two', 'three', 'four'], index=list('abcdef'))
print(df)
print()
print(df.ix[[1,2,4]])
print()
print(df.reindex([1,2,4]))
print()