import pandas as pd

print(pd.date_range('1/1/2011', periods=5))
print()

print(pd.date_range('1/1/2011', periods=5, freq='M'))
print()

print(pd.bdate_range('1/1/2011', periods=5))
print()

start = pd.datetime(2011, 1, 1)
end = pd.datetime(2011, 1, 5)
print(pd.date_range(start, end))