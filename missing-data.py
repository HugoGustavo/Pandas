import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(5,3),
    index=['a', 'c', 'e', 'f', 'h'],
    columns=['one', 'two', 'three']
)
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df)
print()


df = pd.DataFrame(
    np.random.randn(5,3),
    index=['a', 'c', 'e', 'f', 'h'],
    columns=['one', 'two', 'three']
)
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df['one'].isnull())
print()

df = pd.DataFrame(
    np.random.randn(5,3),
    index=['a', 'c', 'e', 'f', 'h'],
    columns=['one', 'two', 'three']
)
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df['one'].notnull())
print()

df = pd.DataFrame(
    np.random.randn(5,3),
    index=['a', 'c', 'e', 'f', 'h'],
    columns=['one', 'two', 'three']
)
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df['one'].sum())
print()

df = pd.DataFrame(index=[0,1,2,3,4,5], columns=['one', 'two'])
print(df['one'].mean())
print()

df = pd.DataFrame(
    np.random.randn(3,3),
    index=['a', 'c', 'e'],
    columns=['one', 'two', 'three']
)
df = df.reindex(['a', 'b', 'c'])
print(df)
print()
print('NaN replaced with 0:')
print(df.fillna(0))
print()

df = pd.DataFrame(
    np.random.randn(5,3),
    index=['a', 'c', 'e', 'f', 'h'],
    columns=['one', 'two', 'three']
)
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df)
print()
print(df.fillna(method='pad'))
print()

df = pd.DataFrame(
    np.random.randn(5,3),
    index=['a', 'c', 'e', 'f', 'h'],
    columns=['one', 'two', 'three']
)
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df)
print()
print(df.fillna(method='bfill'))
print()

df = pd.DataFrame(
    np.random.randn(5,3),
    index=['a', 'c', 'e', 'f', 'h'],
    columns=['one', 'two', 'three']
)
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df)
print()
print(df.dropna())
print()

df = pd.DataFrame(
    np.random.randn(5,3),
    index=['a', 'c', 'e', 'f', 'h'],
    columns=['one', 'two', 'three']    
)
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df.dropna(axis=1))

df = pd.DataFrame({
    'one': [10, 20, 30, 40, 50, 2000],
    'two': [1000, 20, 30, 40, 50, 60]
})
print(df.replace({
    1000:10,
    2000:60
}))