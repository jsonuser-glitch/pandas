import utils
import pandas as pd

info = pd.Series(data=[30, 40, 50])
print(info)
print(info > 40)
print(info[info > 40])