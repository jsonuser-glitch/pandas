import utils
import pandas as pd
target = [1,2,3,4]
sales = [10000, 20000, 30000, 40000]
zonesales = [target, sales]
a = pd.DataFrame(data=zonesales, index=['zoneA', 'zoneB', 'zoneC', 'zoneD'])
print(a)
