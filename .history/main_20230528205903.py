import utils
import pandas as pd

a = {
    'Andhra': {
        'Toys': 7916,
        'Books': 6189,
        'Uniform': 610,
        'Shoes': 8810
    },
    'Odisha': {
        'Toys': 7916,
        'Books': 6189,
        'Uniform': 610,
        'Shoes': 8810
    },
    'M.P': {
        'Toys': 7916,
        'Books': 6189,
        'Uniform': 610,
        'Shoes': 8810
    },
    'U.P': {
        'Toys': 7916,
        'Books': 6189,
        'Uniform': 610,
        'Shoes': 8810
    }
}

b = pd.DataFrame(data=a, index=[1,2,3,4])
# print(b)
print(b[['Books', 'Uniform']])