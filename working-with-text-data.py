import pandas as pd
import numpy as np

series = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234', 'SteveSmith'])
print(series)
print()

series = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234', 'SteveSmith'])
print(series.str.lower())
print()

series = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234', 'SteveSmith'])
print(series.str.upper())
print()

series = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234', 'SteveSmith'])
print(series.str.len())
print()

series = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
print(series)
print('After Stripping: ')
print(series.str.strip())
print()

series = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
print(series)
print('Split Pattern: ')
print(series.str.split(' '))
print()

series = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print(series.str.cat(sep='_'))
print()

series = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print(series.str.contains(' '))
print()

series = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print(series)
print('After replacing @ with $:')
print(series.str.replace('@', '$'))
print()

series = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print(series.str.repeat(2))
print()

series = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print("The number of 'm' in each string:")
print(series.str.count('m'))
print()

series = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print("Strings that star with 'T': ")
print(series.str.startswith('T'))
print()

series = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print("String that end with 't':")
print(series.str.endswith('t'))
print()

series = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print(series.str.findall('e'))
print()

series = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print(series.str.swapcase())
print()

series = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print(series.str.islower())
print()

series = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print(series.str.isupper())
print()

series = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print(series.str.isnumeric())
print()