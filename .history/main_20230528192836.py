import utils
import pandas as pd

a = pd.Series({ 'A': 39, 'B': 41, 'C': 42, 'D': 44 })

print('Tickets amount: ')
print(a[ :2] * 100)