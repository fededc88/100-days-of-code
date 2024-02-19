# grouping and Aggregation

import numpy as np
import pandas as pd

addr ='./Data/mtcars.csv'
cars = pd.read_csv(addr, index_col = 'names')

print(cars.head)

cars_grouped = cars.groupby('cyl')
print(cars_grouped.mean())

#Group the data by the transmission type
cars_grouped = cars.groupby('am')
print(cars_grouped.mean())



