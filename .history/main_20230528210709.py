import utils
import pandas as pd

ser1 = pd.Series([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000])
print(ser1[ser1 > 2000])