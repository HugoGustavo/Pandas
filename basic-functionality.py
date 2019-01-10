import pandas as pd
import numpy as np

serie = pd.Series(np.random.randn(4))
print(serie)
print()

serie = pd.Series(np.random.randn(4))
print('The axes are: ')
print(serie.axes)
print()

serie = pd.Series(np.random.randn(4))
print('The the object empty? ')
print(serie.empty)
print()

serie = pd.Series(np.random.randn(4))
print(serie)
print('The dimensions of the object: ')
print(serie.ndim)
print()

serie = pd.Series(np.random.randn(2))
print(serie)
print('The size of the object: ')
print(serie.size)
print()

serie = pd.Series(np.random.randn(4))
print(serie)
print('The actual data series is: ')
print(serie.values)

serie = pd.Series(np.random.randn(4))
print('The original series is: ')
print(serie)
print('The first two rows of the data series: ')
print(serie.head(2))
print()

serie = pd.Series(np.random.randn(4))
print(serie)
print('The last two rows of the data series: ')
print(serie.tail(2))
print()

data = {
    'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
    'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
    'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.2, 4.6, 3.8])
}
df = pd.DataFrame(data)
print('Our data series is: ')
print(df)
print()

data = {
    'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
    'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
    'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.2, 4.6, 3.8])
}
df = pd.DataFrame(data)
print('The transpose of the data series is: ')
print(df.T)

data = {
    'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
    'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
    'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.2, 4.6, 3.8])
}
df = pd.DataFrame(data)
print('Row axis labels and column axis labels are: ')
print(df.axes)
print()

data = {
    'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
    'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
    'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.2, 4.6, 3.8])
}
df = pd.DataFrame(data)
print('The data types of each column are: ')
print(df.dtypes)
print()

data = {
    'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
    'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
    'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.2, 4.6, 3.8])
}
df = pd.DataFrame(data)
print('Is the object empty? ')
print(df.empty)
print()

data = {
    'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
    'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
    'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.2, 4.6, 3.8])
}
df = pd.DataFrame(data)
print('Our object is: ')
print(df)
print('The dimensions of the object is: ')
print(df.ndim)
print()

data = {
    'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
    'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
    'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.2, 4.6, 3.8])
}
df = pd.DataFrame(data)
print('Our object is: ')
print(df)
print('The dimensions of the object is: ')
print(df.ndim)
print()

data = {
    'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
    'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
    'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.2, 4.6, 3.8])
}
df = pd.DataFrame(data)
print('Our object is: ')
print(df)
print('The dimensions of the object is: ')
print(df.shape)
print()

data = {
    'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
    'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
    'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.2, 4.6, 3.8])
}
df = pd.DataFrame(data)
print('Our object is: ')
print(df)
print('The total number of elements in our object is: ')
print(df.size)
print()

data = {
    'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
    'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
    'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.2, 4.6, 3.8])
}
df = pd.DataFrame(data)
print('Our object is: ')
print(df)
print('The actual data in our data frame is: ')
print(df.values)
print()

data = {
    'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
    'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
    'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.2, 4.6, 3.8])
}
df = pd.DataFrame(data)
print('Our object is: ')
print(df)
print('The first two rows of the data frame is: ')
print(df.head(2))
print()

data = {
    'Name': pd.Series(['Tom', 'James', 'Ricky', 'Vin', 'Steve', 'Smith', 'Jack']),
    'Age': pd.Series([25, 26, 25, 23, 30, 29, 23]),
    'Rating': pd.Series([4.23, 3.24, 3.98, 2.56, 3.2, 4.6, 3.8])
}
df = pd.DataFrame(data)
print('Our data frame is: ')
print(df)
print('The last two rows of the data frame is: ')
print(df.tail(2))
print()