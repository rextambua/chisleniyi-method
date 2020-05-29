# Студент: Тамбуа Рекс Тамиганг, НП301
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

# f - function
# df - its derivative


def Newton(f, df, x0, tolerance=1e-10, verbose=False, N_max=100):
    ### your solution is here
    error = 100
    i = 0
    while error > tolerance and i < N_max:
        x0 -= f(x0) / df(x0)
        error = abs(f(x0))
        i += 1
        if verbose:
            print(f'Iteration {i}, error = {error:.2}, x = {x0:.8}.')
    return x0

f = lambda z: z**3 -1
df = lambda z: 3*z**2

Newton(f, df, 4, tolerance=1e-10, verbose=True)
print('\n')

N = 1000
t = np.linspace(-1, 1, N)
x, y = np.meshgrid(t, t)
x = x.reshape(-1,)
y = y.reshape(-1,)
z = x + 1j*y

points = []
for p in z:
    solution = Newton(f, df, p)
    points.append(solution)
points = np.hstack(points).reshape(N, N)
points = np.real(np.cos(points)*np.sin(np.imag(points)))

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.imshow(points, cmap='inferno')
ax.axis('off');
