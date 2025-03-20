import random
import matplotlib.pyplot as plt
import math

import numpy as np


def drawNumber(n):
    x = []
    y = []
    for i in range(n):
        x.append(random.random())
        y.append(random.random())
    return x,y

def inCircVerify(x,y,ax1,ax2):
    inCircX = []
    inCircY = []
    outCircX = []
    outCircY = []
    #circle = plt.Circle((0,0), 1, color='black', fill=False)

    for i in range(len(y)):
        if y[i] <= math.sqrt(1 - x[i]**2):
            inCircX.append(x[i])
            inCircY.append(y[i])
        else:
            outCircX.append(x[i])
            outCircY.append(y[i])

    calc_pi = len(inCircX)/len(y)*4
    pis.append(calc_pi)

    # ax[ax1, ax2].scatter(inCircX, inCircY, color='red',s=5)
    # ax[ax1, ax2].scatter(outCircX,outCircY,color='blue',s=5)
    # ax[ax1, ax2].add_patch(circle)
    # ax[ax1, ax2].set_xlim((0, 1))
    # ax[ax1, ax2].set_ylim((0, 1))

# [X1,Y1] = drawNumber(100)
# [X2,Y2] = drawNumber(1000)
# [X3,Y3] = drawNumber(10000)
# [X4,Y4] = drawNumber(100000)
#
#
# fig,ax = plt.subplots(2,2)
# inCircVerify(X1,Y1,0,0)
# inCircVerify(X2,Y2,0,1)
# inCircVerify(X3,Y3,1,0)
# inCircVerify(X4,Y4,1,1)
# plt.show()
pis = []
for i in range(100,100000):
    print(i)
    [X,Y] = drawNumber(i)
    inCircVerify(X,Y,0,0)

plt.plot(pis)
plt.show()