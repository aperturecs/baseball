#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
'''
y = list()

for val in range(0, 5):
    y.append(np.sin(x[val]))
'''
y = np.sin(x)
for val in range(0, 5):
    print "(%d, %lf)" % (x[val], y[val])

plt.plot(x, y, "ro") # ro : 점
plt.show()
