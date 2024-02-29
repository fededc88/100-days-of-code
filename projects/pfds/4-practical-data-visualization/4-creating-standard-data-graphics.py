import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

# Creating a line chart in matplotlib

x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]

#plt.plot(x,y)
#plt.show()

# Plotting a line chart from a Pandas object

address = 'C:\\Users\\CECCAFDE\\workspace\\sadbox\\100-days-of-code\\projects\\pfds\\Data\\mtcars.csv'
cars = pd.read_csv(address)

print(cars.head)

mpg = cars['mpg']
#mpg.plot()
#plt.show()

df = cars[['cyl','wt','mpg']]
#df.plot()
#plt.show()

# Create a bar char

#plt.bar(x,y)
#plt.show()

#mpg.plot(kind = 'bar')
#mpg.plot(kind = 'barh')

# Creating a pie Chart
plt.pie(x)
#plt.show()

# Saving a plot
plt.savefig('pie_chart.png')

