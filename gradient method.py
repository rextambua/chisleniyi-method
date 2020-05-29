### First Part
### Студент: Тамбуа Рекс Тамиганг, НП301
import numpy as np
%matplotlib notebook
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

f = lambda x, y: 1 - np.cos(x)*np.cos(y)

xi = np.linspace(-5, 5, 100)
yi = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(xi, yi, sparse = True)
Z = f(X,Y)

fig = plt.figure()
ax3D = fig.add_subplot(111, projection='3d')
ax3D.plot_surface(X, Y, Z, alpha=0.8)  
ax3D.set_xlabel("x")
ax3D.set_ylabel("y")
ax3D.set_zlabel("z")

### Second Part
def grad(x = 0, y = 3, h = 0.01, n = 640, f = f, X = X, Y = Y, Z = Z):
    x_step = []
    y_step = []
    for _ in range(n):
        x -= h * np.sin(x) * np.cos(y)
        x_step.append(x)
        y -= h * np.cos(x) * np.sin(y)
        y_step.append(y)

    fig = plt.figure()
    ax3D = fig.add_subplot(111, projection='3d')
    ax3D.plot_surface(X, Y, Z, alpha=0.8)  
    ax3D.scatter3D(x_step, y_step, f(x_step, y_step), s = 40, c = 'r')
    ax3D.set_xlabel("x")
    ax3D.set_ylabel("y")
    ax3D.set_zlabel("z")
grad()


#### Third part
def grad1(x = 0, y = 3, h = 0.01, n = 640, f = f, X = X, Y = Y, Z = Z):
    x_step = []
    y_step = []
    for _ in range(n):
        x -= f(x + h/2, y) - f(x - h/2, y)
        x_step.append(x)
        y -= f(x, y + h/2) - f(x, y - h/2)
        y_step.append(y)

    # %matplotlib notebook
    fig = plt.figure()
    ax3D = fig.add_subplot(111, projection='3d')
    ax3D.plot_surface(X, Y, Z, alpha=0.8)  
    ax3D.scatter3D(x_step, y_step, f(x_step, y_step), s = 40, c = 'r')
    ax3D.set_xlabel("x")
    ax3D.set_ylabel("y")
    ax3D.set_zlabel("z")
grad1()

### Last One
def grad2(x = 0.5, y = 3.5, h = 0.01, alpha = 0.0001, f = f, X = X, Y = Y):
    Z = f(X, Y)

    x_old = 0
    y_old = 0
    x_step = []
    y_step = []
    i = 0
    while abs(f(x, y) - f(x_old, y_old))  > alpha:
        x_old = x
        y_old = y
        x -= h * np.sin(x) * np.cos(y)
        x_step.append(x)
        y -= h * np.cos(x) * np.sin(y)
        y_step.append(y)
        i+=1
    print(i)

    fig = plt.figure()
    ax3D = fig.add_subplot(111, projection='3d')
    ax3D.plot_surface(X, Y, Z, alpha=0.8)  
    ax3D.scatter3D(x_step, y_step, f(x_step, y_step), s = 40, c = 'r')
    ax3D.set_xlabel("x")
    ax3D.set_ylabel("y")
    ax3D.set_zlabel("z")
grad2()