import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(10))
ts[2:-2] = np.nan
sts = ts.to_sparse()
print(sts)
print()

df = pd.DataFrame(np.random.randn(10000, 4))
df.ix[:9998] = np.nan
sdf = df.to_sparse()
print(sdf.density)
print()

ts = pd.Series(np.random.randn(10))
ts[2:-2] = np.nan
sts = ts.to_sparse()
print(sts.to_dense())
print()

s = pd.Series([1, np.nan, np.nan])
print(s)
print()
s.to_sparse()
print(s)
print()