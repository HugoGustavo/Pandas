import pandas as pd
import numpy as np

series = pd.Series(['a', 'b', 'c', 'a'], dtype='category')
print(series)
print()

category = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
print(category)
print()

category = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c', 'd'], ['c', 'b', 'a'])
print(category)
print()

category = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c', 'd'], ['c', 'b', 'a'], ordered=True)
print(category)
print()

category = pd.Categorical(['a', 'c', 'c', np.nan], categories=['b', 'a', 'c'])
df = pd.DataFrame({
    'category': category,
    'series': ['a', 'c', 'c', np.nan]
})
print(df.describe())
print()
print(df['category'].describe())
print()

series = pd.Categorical(['a', 'c', 'c', np.nan], categories=['b', 'a', 'c'])
print(series.categories)
print()

category = pd.Categorical(['a', 'c', 'c', np.nan], categories=['b', 'a', 'c'])
print(category.ordered)
print()

series = pd.Series(['a', 'b', 'c', 'a'], dtype='category')
series.cat.categories = ["Group %s" % group for group in series.cat.categories]
print(series.cat.categories)
print()

series = pd.Series(['a', 'b', 'c', 'a'], dtype='category')
series = series.cat.add_categories([4])
print(series.cat.categories)
print()

series = pd.Series(['a', 'b', 'c', 'a'], dtype='category')
print('Original object:')
print(series)
print()
print('After removal:')
print(series.cat.remove_categories('a'))
print()

category1 = pd.Series([1,2,3]).astype('category', categories=[1,2,3], ordered=True)
category2 = pd.Series([2,2,2]).astype('category', categories=[1,2,3], ordered=True)
print( category1 > category2 )
print()