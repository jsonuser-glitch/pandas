import utils
import pandas as pd
a = pd.DataFrame({
    'Delhi': { 'Population': 'A', 'Hospitals': 'B' },
    'Mumbai': { 'Population': 'C', 'Hospitals': 'D' }
})
del a['Population']
a = a.drop(['Bangalore'])
print(a)