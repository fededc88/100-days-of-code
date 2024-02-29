import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# define axes, ticks, and grids
x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]

fig = plt.figure()

ax = fig.add_axes([.1,.1,1,1])

ax.plot(x, y)

fig2 = plt.figure()
ax2 = fig2.add_axes([.1,.1,1,1])
ax2.set_xlim([1,9])
ax2.set_ylim([0,5])

ax2.set_xticks([0,1,2,3,4,5,6,8,9,10])
ax2.set_yticks([0,1,2,3,4,5])
ax2.grid()
ax2.plot(x,y)

#fig3 = plt.figure()
fig3, (ax4, ax5) = plt.subplots(1,2)

ax4.plot(x)
ax5.plot(x,y)

plt.show()


