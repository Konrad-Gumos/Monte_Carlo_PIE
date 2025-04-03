import matplotlib.pyplot as plt
import numpy as np


def drawNumber(n):
    # drawing two sets of random numbers - coordinates
    x = np.random.rand(n)
    y = np.random.rand(n)
    return x,y

def inCircVerify(x,y):
    global inCircle # indicator whether the point is placed within circle or outside
    inCircle = y <= np.sqrt(1 - x ** 2)
    calc_pi = (inCircle.sum() / inCircle.size) * 4 # calculated value of pi
    return calc_pi

def drawFigures(ax1,ax2,x,y,calc_pi):
    # function for drawing graphs presenting points, red markers represent points outside circle, while blue are those placed inside
    circle = plt.Circle((0,0), 1, color='black', fill=False)
    ax[ax1, ax2].scatter(x[~inCircle], y[~inCircle], color='red', s=5)
    ax[ax1, ax2].scatter(x[inCircle], y[inCircle], color='blue', s=5)

    ax[ax1, ax2].add_patch(circle)

    ax[ax1, ax2].set_xlim((0, 1))
    ax[ax1, ax2].set_ylim((0, 1))
    ax[ax1, ax2].set_aspect('equal')
    ax[ax1, ax2].set_title(f'n = {x.size}, pi = {calc_pi}')
    plt.subplots_adjust(hspace = 0.5)

[X1,Y1] = drawNumber(100)
[X2,Y2] = drawNumber(1000)
[X3,Y3] = drawNumber(10000)
[X4,Y4] = drawNumber(100000)

fig,ax = plt.subplots(2,2)
drawFigures(0,0,X1,Y1,inCircVerify(X1,Y1))
drawFigures(0,1,X2,Y2,inCircVerify(X2,Y2))
drawFigures(1,0,X3,Y3,inCircVerify(X3,Y3))
drawFigures(1,1,X4,Y4,inCircVerify(X4,Y4))
plt.show()

pis = []
for k in range(100,1000):
    [X,Y] = drawNumber(k)
    pis.append(inCircVerify(X,Y))

plt.plot(pis)
plt.title("Wykres wyznaczanej wartości dla liczby losowanych punktów")
plt.hlines(3.14,0,1000,color="red",label="3.14")
plt.xlabel("Liczba losowanych punktów")
plt.ylabel("Wyznaczana wartość")
plt.show()

ns = [100000,250000,500000,750000,1000000]
data = [[inCircVerify(drawNumber(n)[0],drawNumber(n)[1]) for _ in range(10)] for n in ns]
print(data)
plt.boxplot(data)
plt.hlines(3.14,0,6,color="red",label="3.14",linestyles="dashed")
# plt.xticks(ns)
plt.xlabel("Liczba losowanych punktów")
plt.ylabel("Wyznaczana wartość")
plt.show()