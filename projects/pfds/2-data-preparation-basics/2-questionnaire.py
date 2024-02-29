
import numpy as np
import pandas as pd

# 1
addr ='./Data/mtcars.csv'
cars = pd.read_csv(addr, index_col = 'names')

#Group the data by the transmission type
cars_grouped = cars.groupby('am')
print(cars_grouped.mean())

# 2
df_obj = pd.DataFrame(np.arange(25).reshape(5,5))

df_obj.loc[0:3,1] = np.nan
print(df_obj)

print(df_obj.isna().sum())

print(df_obj.isnull().sum())
df_obj = df_obj.dropna(axis=1)
print(df_obj)

# 3
df_1 = pd.DataFrame(np.array([[1.,3.,4.],[2.,5.,2.,],[0.,4.,1.,]]))
df_2 = pd.DataFrame(np.array([[2.,1.],[0.,5.],[4.,7.]]))

print(pd.concat([df_1, df_2]))

#4
df_obj = pd.DataFrame(np.arange(20,31))
print(df_obj)

print(df_obj[df_obj < 25])

#5

print(df_obj < 25)

#9

df_obj = pd.DataFrame(np.arange(9).reshape(3,3))
df_obj.loc[2,2] = np.nan

x = df_obj.fillna({2:9})
print(df_obj)
print(x)



