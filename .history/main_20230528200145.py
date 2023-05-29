import utils
import pandas as pd

a = {
    'section': ['A', 'B', 'C', 'D'],
    'contribution': [6700, 5600, 5000, 5200]
}

b = pd.DataFrame(a)

print(b)