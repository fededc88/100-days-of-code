
import numpy as np
import pandas as pd

from pandas import Series, DataFrame

print(np.arange(8))

series_obj = Series(np.arange(8), index=['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6', 'row 7', 'row 8'])

print(series_obj)

# Selection element with row index

element = series_obj['row 7']
print('element selected', element)

# Selection multimple elements of a Series with row index
elements = series_obj[[0, 7]]
print(elements)

np.random.seed(100)
df_obj = DataFrame(np.random.rand(36).reshape((6,6)),
    index=['row 1', 'row 2','row 3', 'row 4', 'row 5', 'row 6'], 
    columns=['col 1', 'col 2', 'col 3', 'col 4', 'col 5', 'col 6'])

print(df_obj)

fil_def_obj = df_obj.loc[['row 2', 'row 5'], ['col 2', 'col 5']]
print(fil_def_obj)

# Data Slicing
ser_slice = series_obj['row 2':'row 6']
print(ser_slice)

# Comparing with scalars
compare_df_obj = df_obj < .2
print(compare_df_obj)

filter_df_obj = df_obj[df_obj<0.2]
print(filter_df_obj)

series_obj.loc[['row 2', 'row 3', 'row 5']] = 18
print(series_obj)











