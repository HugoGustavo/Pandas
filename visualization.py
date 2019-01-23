import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10,4),
    index=pd.date_range('1/1/2000', periods=10),
    columns=list('ABCD')
)
df.plot()

df = pd.DataFrame(
    np.random.randn(10,4),
    columns=['a', 'b', 'c', 'd']
)
df.plot.bar()

df = pd.DataFrame(
    np.random.rand(10,4),
    columns=['a', 'b', 'c', 'd']
)
df.plot.bar(stacked=True)

df = pd.DataFrame(
    np.random.rand(10,4),
    columns=['a', 'b', 'c', 'd']
)
df.plot.barh(stacked=True)

df = pd.DataFrame({
    'a': np.random.randn(1000)+1,
    'b': np.random.randn(1000),
    'c': np.random.randn(1000)-1
}, columns=['a', 'b', 'c'])
df.plot.hist(bins=20)

df = pd.DataFrame({
    'a': np.random.randn(1000)+1,
    'b': np.random.randn(1000),
    'c': np.random.randn(1000)-1
}, columns=['a', 'b', 'c'])
df.diff.hist(bins=20)

df = pd.DataFrame(
    np.random.rand(10,5),
    columns=['A', 'B', 'C', 'D', 'E']
)
df.plot.box()

df = pd.DataFrame(
    np.random.rand(10,4),
    columns=['a', 'b', 'c', 'd']
)
df.plot.area()

df = pd.DataFrame(
    np.random.rand(50,4),
    columns=['a', 'b', 'c', 'd']
)
df.plot.scatter(x='a', y='b')

df = pd.DataFrame(
    3 * np.random.rand(4),
    index=['a', 'b', 'c', 'd'],
    columns=['x']
)
df.plot.pie(subplots=True)