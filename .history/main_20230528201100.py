import utils
import pandas as pd

zoneA = {
    'Target': '56000',
    'Sales': '58000'
}

zoneB = {
    'Target': '56000',
    'Sales': '58000'
}

zoneC = {
    'Target': '56000',
    'Sales': '58000'
}

zoneD = {
    'Target': '56000',
    'Sales': '58000'
}

sales = [ zoneA, zoneB, zoneC, zoneD ]

a = pd.DataFrame(data=sales, index=['zoneA', 'zoneB', 'zoneC', 'zoneD'])

print(a)