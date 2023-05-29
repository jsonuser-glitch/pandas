import pandas as pd

a = pd.Series([2, 3, 4, 5, 6])
b = a ** 2
print(b[b > 15])