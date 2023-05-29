import pandas as pd
a = ['A', 'B', 'C', 'D']
b = ['1000', '2000', '3000', '4000']
s = pd.Series(data=b, index=a)
print(s)