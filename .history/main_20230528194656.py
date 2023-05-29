import utils
import pandas as pd

population = pd.Series([102967, 156637, 178982, 908727], index=['MH', 'GA', 'KL', 'KA'])
avgincome = pd.Series([29188, 908762, 231221, 890289], index=['MH', 'GA', 'KL', 'KA'])

percapita = avgincome / population

print('Population: ')
print(population)
print('Average Income')
print(avgincome)
print('Per Capita Income')
print(percapita)