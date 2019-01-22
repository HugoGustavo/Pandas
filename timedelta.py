import pandas as pd

print(pd.Timedelta('2 days 2 hours 15 minutes 30 seconds'))
print()

print(pd.Timedelta(6, unit='h'))
print()

print(pd.Timedelta(days=2))
print()

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([pd.Timedelta(days=i) for i in range(3)])
df = pd.DataFrame(dict(A=s, B=td))
print(df)
print()

s = pd.Series(pd.date_range('2012-01-01', periods=3, freq='D'))
td = pd.Series([pd.Timedelta(days=i) for i in range(3)])
df = pd.DataFrame(dict(A=s, B=td))
df['C'] = df['A'] + df['B']
print(df)
print()

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A=s, B=td))
df['C'] = df['A'] - df['B']
df['D'] = df['C'] - df['B']
print(df)
print()