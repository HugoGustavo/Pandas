import pandas as pd

df = pd.DataFrame()
print(df)
print()

data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data)
print(df)
print()

data = [
    ['Alex', 10],
    ['Bob', 12],
    ['Clarke', 13]
]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)
print()

data = [
    ['Alex', 10],
    ['Bob', 12],
    ['Clarke', 13]
]
df = pd.DataFrame(data, columns=['Name', 'Age'], dtype=float)
print(df)
print()

data = {
    'Name': ['Tom', 'Jack', 'Steve', 'Ricky'],
    'Age': [28, 34, 29, 42]
}
df = pd.DataFrame(data)
print(df)
print()

data = {
    'Name': ['Tom', 'Jack', 'Steve', 'Ricky'],
    'Age': [28, 34, 29, 42]
}
df = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])
print(df)
print()

data =[
    {'a':1, 'b':2},
    {'a':5, 'b':10, 'c':20}
]
df = pd.DataFrame(data)
print(df)
print()

data = [
    {'a':1, 'b':2},
    {'a':5, 'b':10, 'c':20}
]
df = pd.DataFrame(data, index=['first', 'second'])
print(df)
print()

data = [
    {'a':1, 'b':2},
    {'a':5, 'b':10, 'c':20}
]
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a','b'])
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print(df1)
print()
print(df2)
print()

data = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
}
df = pd.DataFrame(data)
print(df)
print()

data = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
}
df = pd.DataFrame(data)
print(df['one'])
print()

data = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
}
df = pd.DataFrame(data)
print('Adding new column by passin as Series')
df['three'] = pd.Series([10,20,30], index=['a', 'b', 'c'])
print(df)
print('Adding a new columns using the existing columns in DataFrame')
df['four'] = df['one'] + df['three']
print(df)
print()

data = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
    'three': pd.Series([10, 20, 30], index=['a', 'b', 'c'])
}
df = pd.DataFrame(data)
print('Our dataframe is: ')
print(df)
print('Deleting the first column using DEL function: ')
del(df['one'])
print(df)
print('Deleting another columns using POP function: ')
df.pop('two')
print(df)
print()

data = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
}
df = pd.DataFrame(data)
print(df.loc['b'])
print()

data = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
}
df = pd.DataFrame(data)
print(df.iloc[2])
print()

data = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
}
df = pd.DataFrame(data)
print(df[2:4])
print()

df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])
df2 = pd.DataFrame([[5,6], [7,8]], columns=['a', 'b'])
df = df.append(df2)
print(df)
print()

df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])
df2 = pd.DataFrame([[5,6], [7,8]], columns=['a', 'b'])
df = df.append(df2)
df = df.drop(0)
print(df)