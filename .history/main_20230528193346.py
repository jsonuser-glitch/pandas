import utils
import pandas as pd

a = pd.Series(data=[30,40,50], index=['Science', 'Huamnities', 'Commerce'])
b = pd.Series(data=[37, 44, 45], index=['Science', 'Commerce', 'Humanities'])

print('Total no. of students: ', a + b)
