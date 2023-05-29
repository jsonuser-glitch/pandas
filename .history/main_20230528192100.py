import utils
import pandas as pd

section = ['A', 'B', 'C', 'D']
contribution = [6700, 5600, 5000, 5200]

a = pd.Series(data=contribution, index=section)
print(a)