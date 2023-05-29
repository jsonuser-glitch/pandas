import utils
import pandas as pd
a = pd.DataFrame({
    'Delhi': { 'Population': 'A', 'Hospitals': 'B' },
    'Mumbai': { 'Population': 'C', 'Hospitals': 'D' }
})
print(a.T)
# del a['Population']
# a = a.drop(['Mumbai'])
# print(a)