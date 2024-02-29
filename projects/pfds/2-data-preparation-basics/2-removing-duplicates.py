import numpy as np
import pandas as pd

df_obj = pd.DataFrame({'column 1':[1,1,2,2,3,3,3],
                       'column 2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
                       'column 3': ['A', 'A', 'B', 'B', 'C', 'C', 'C']})

print(df_obj)

# is duplicate
print(df_obj.duplicated())

# Drop duplicated
print(df_obj.drop_duplicates())

df_obj = pd.DataFrame({'column 1':[1,1,2,2,3,3,3],
                       'column 2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
                       'column 3': ['A', 'A', 'B', 'B', 'C', 'D', 'C']})

print(df_obj.drop_duplicates(['column 3']))

