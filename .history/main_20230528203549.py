import utils
import pandas as pd

a = pd.DataFrame({
    'wt': [42, 75, 66],
    'name': ['arnav', 'charles', 'guru'],
    'age': [15,22,35]
})

print('original dataframe:' )
print(a)

print('Transpose': )
print(a.T)