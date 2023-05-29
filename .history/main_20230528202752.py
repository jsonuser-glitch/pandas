import utils
import pandas as pd

target = [1,2,3,4]
sales = [5,6,7,8]
zonesales = [target, sales]
df = pd.DataFrame(data=zonesales, columns=['A', 'B', 'C', 'D'], index=['Target', 'Sales'])
print(df)