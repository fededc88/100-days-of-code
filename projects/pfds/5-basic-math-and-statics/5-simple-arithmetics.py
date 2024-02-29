import numpy as np

import pandas as pd

# creating arrays 
a = np.array([1,2,3,4,5,6])
print('a:', a)

b = np.array([[10,20,30],[40,50,60]])
print('b:', b)

np.random.seed(25)
c = 36*np.random.randn(6)
print('c: ', c)

d = np.arange(1,35)
print('d:', d)

# Performing arithmetics

print('a * 10 =', a*10)

print('c + a =', c + a)

print('c - a =', c - a)

print('c * a =', c * a)

print('c / a =', c / a)

cars = pd.read_csv('../Data/mtcars.csv')

print(cars.describe())

a = np.array([[1.,3.],[2.,4.]])
b = np.array([[5.,8.],[7.,9.]])
print('a*b =', a*b)

x = np.array([1,2,7])
y = np.array([3,8,9])

dot = np.dot(x,y)
print(dot)

xx=np.array([[7.,9.],[5.,12.]])
yy=np.array([[2.,8.],[7.,4.]])

print(np.matmul(xx,yy))

xx=np.array([[1.,2.,3.],[4.,5.,6.]])
yy=np.array([[10.,11.],[20.,21.],[30.,31.]])

print(np.matmul(xx,yy))

a=np.array([1,8,2,6,3,8,5,5,5,5])
b=np.array([17,16,20,18,22,15,21,15,17,22])

print ('(a+b)/10=', (a+b)/10)

print(cars.groupby(['vs', 'cyl']).count())

vs = cars['vs']
cyl = cars['cyl']

print(pd.crosstab(vs,cyl))






