import pandas as pd
import numpy as np

data = np.random.rand(2,4,5)
panel = pd.Panel(data)
print(panel)
print()

data = {
    'Item1': pd.DataFrame(np.random.randn(4,3)),
    'Item2': pd.DataFrame(np.random.randn(4,2))
}
panel = pd.Panel(data)
print(panel)
print()

panel = pd.Panel()
print(panel)
print()

data = {
    'Item1': pd.DataFrame(np.random.randn(4,3)),
    'Item2': pd.DataFrame(np.random.randn(4,2))
}
panel = pd.Panel(data)
print(panel['Item1'])
print()

data = {
    'Item1': pd.DataFrame(np.random.randn(4,3)),
    'Item2': pd.DataFrame(np.random.randn(4,2))
}
panel = pd.Panel(data)
print(panel.major_xs(1))
print()



data = {
    'Item1': pd.DataFrame(np.random.randn(4,3)),
    'Item2': pd.DataFrame(np.random.randn(4,2))
}
panel = pd.Panel(data)
print(panel.minor_xs(1))