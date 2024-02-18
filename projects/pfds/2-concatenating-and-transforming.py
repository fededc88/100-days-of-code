# Concatenate and Transform Data

import numpy as np
import pandas as pd

df_obj = pd.DataFrame(np.arange(36).reshape(6,6))
print(df_obj)

df_2_obj = pd.DataFrame(np.arange(15).reshape(5,3))
print(df_2_obj)

# Concatenating data
conc_obj = pd.concat([df_obj, df_2_obj], axis=1)
print(conc_obj)

print(conc_obj[0])

conc_obj = pd.concat([df_obj, df_2_obj])
print(conc_obj)

#Transformin Data

print(df_obj.drop([0,2]))

print(df_obj.drop([0,2], axis = 'columns'))

# Adding data

series_obj = pd.Series(np.arange(6))
series_obj.name = 'added_variable'

print(series_obj)

variable_added = pd.DataFrame.join(df_obj, series_obj)
print(variable_added)

# pd.DataFrame.append has been deprecated.
#added_db = variable_added.append(variable_added, ignore_index = False)
#print(added_db)

# Sorting Data

print('dfobj')
print(df_obj)
print('df_sorted')
fd_sorted = df_obj.sort_values(by = 5, ascending=False)
print(fd_sorted)
