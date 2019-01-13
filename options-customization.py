import pandas as pd

print(pd.get_option('display.max_rows'))

print(pd.get_option('display.max_columns'))

pd.set_option('display.max_rows', 80)
print(pd.get_option('display.max_rows'))

pd.set_option('display.max_columns', 30)
print(pd.get_option('display.max_columns'))

pd.reset_option('display.max_rows')
print(pd.get_option('display.max_rows'))

pd.describe_option('display.max_rows')

with pd.option_context('display.max_rows', 10):
    print(pd.get_option('display.max_rows'))
print(pd.get_option('display.max_rows'))