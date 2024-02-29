import numpy as np
import pandas as pd

from pandas import Series, DataFrame

# Figuring out what data is missing

missing = np.nan

series_obj = Series(['Row 1', 'Row 2', missing, 'Row 4', 'Row 5', 'Row 6', missing, 'Row 8']) 
print(series_obj)

print(series_obj.isnull())

# Filling in for missing values
np.random.seed(25)
df_obj = DataFrame(np.random.rand(36).reshape(6,6))
print(df_obj)

# Generate NaN values 
df_obj.loc[3:5, 0] = missing
df_obj.loc[1:4, 5] = missing
print(df_obj)

# fill Nan values

#df_obj.fillna(0, inplace=True)
filled_df = df_obj.fillna(0)
print(filled_df)

filled_df = df_obj.fillna({0:1, 5:1.25})
print(filled_df)

# Filling Nan with ffill() and bfill() methods
filled_df = df_obj.ffill()
print(filled_df)

# Counting Missing values

print(df_obj.isnull().sum())

# Filtering out missing values

no_na_df = df_obj.dropna()
print(no_na_df)

no_na_df = df_obj.dropna(axis='columns')
print(no_na_df)

