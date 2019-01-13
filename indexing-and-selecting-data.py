import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(8,4),
    index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
    columns = ['A', 'B', 'C', 'D']    
)
print(df.loc[:, 'A'])
print()

df = pd.DataFrame(
    np.random.randn(8,4),
    index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
    columns = ['A', 'B', 'C', 'D']
)
print(df.loc[:, ['A', 'C']])
print()

df = pd.DataFrame(
    np.random.randn(8,4),
    index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
    columns = ['A', 'B', 'C', 'D']
)
print(df.loc[['a', 'b', 'f', 'h'], ['A', 'C']])
print()

df = pd.DataFrame(
    np.random.randn(8,4),
    index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
    columns = ['A', 'B', 'C', 'D']
)
print(df.loc['a':'h'])
print()

df = pd.DataFrame(
    np.random.randn(8,4),
    index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
    columns = ['A', 'B', 'C', 'D']
)
print(df.loc['a']>0)
print()

df = pd.DataFrame(np.random.randn(8,4), columns=['A', 'B', 'C', 'D'])
print(df.iloc[:4])
print()

df = pd.DataFrame(np.random.randn(8,4), columns=['A', 'B', 'C', 'D'])
print(df.iloc[:4])
print()
print(df.iloc[1:5, 2:4])
print()

df = pd.DataFrame(np.random.randn(8,4), columns=['A', 'B', 'C', 'D'])
print(df.iloc[[1, 3, 5], [1, 3]])
print()
print(df.iloc[1:3, :])
print()
print(df.iloc[:, 1:3])
print()

df = pd.DataFrame(np.random.randn(8,4), columns=['A', 'B', 'C', 'D'])
print(df.ix[:4])
print()

df = pd.DataFrame(np.random.randn(8,4), columns=['A', 'B', 'C', 'D'])
print(df.ix[:, 'A'])
print()

df = pd.DataFrame(np.random.randn(8,4), columns=['A', 'B', 'C', 'D'])
print(df['A'])
print()

df = pd.DataFrame(np.random.randn(8,4), columns=['A', 'B', 'C', 'D'])
print(df[['A', 'B']])
print()

df = pd.DataFrame(np.random.randn(8,4), columns=['A', 'B', 'C', 'D'])
print(df[2:2])
print()

df = pd.DataFrame(np.random.randn(8,4), columns=['A', 'B', 'C', 'D'])
print(df.A)
print()