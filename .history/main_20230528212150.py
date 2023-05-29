import utils
import pandas as pd

a = pd.DataFrame({
    'zoneA': { 'Target': 56000, 'Sales': 58000 },
    'zoneB': { 'Target': 56000, 'Sales': 58000 },
    'zoneC': { 'Target': 56000, 'Sales': 58000 },
    'zoneD': { 'Target': 56000, 'Sales': 58000 }
})
# print(a)

a['orders'] = ['1000', '2000', '3000', '4000']