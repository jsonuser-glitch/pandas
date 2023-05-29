import utils
import pandas as pd
a = {
    'yr1': {
        'Qtr1': '34500',
        'Qtr2': '56000'
    },
    'yr2': {
        'Qtr1': '44900',
        'Qtr2': '46100'
    }
}

df = pd.DataFrame(a)
print(df)