# imports
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numba import njit
# user input
# make a check so user can only input integers
print('Target Coordinates')
x_ui = float(input('Input x co-ordinate [m]\n'))
if x_ui == 0:
    x_ui = 0.001
y_ui = float(input('Input y co-ordinate [m]\n'))
if y_ui == 0:
    y_ui = 0.001
z_ui = float(input('Input z co-ordinate [m]\n'))
if z_ui == 0:
    z_ui == 0.001
t_ui = float(input("Input time of flight [s]\n"))
if t_ui == 0:
    t_ui = 0.001
# define inital conditions
g = 9.8  # acceleration due to gravity [m/s^2]
dt = 0.01  # timestep [s]
theta = np.arctan(y_ui / z_ui)
phi = np.arctan(y_ui / x_ui)


# determine minimum velocity
def vel(x, y, t, a, b):
    v = g * t * x / (y * (np.cos(a) - np.cos(b)) * t_ui)
    return v
veli = vel(x_ui, y_ui, t_ui, theta, phi)
print('Veloticy = ', veli)

# def RK4(f, x, y, h):
#    k1 = h*f(x,y)
#    k2 = h*f(x+(h/2), (y+(k1/2)))
#    k3 = h*f(x+(h/2), (y+(k2/2)))
#    k4 = h*f((x+h), (y+k3))
#    y = y + (k1 + (2*k2) + (2*k3) + k4)/6
#    return y
@njit
def xmotion(v, t):
    """
    :param v: initial velocity [m/s]
    :param t: Time [s]
    :return: Velocity in x direction [m/s], position in x direction [m]
    """
    ux = np.round(v * t, 1)
    sx = np.round(ux * t, 1)
    return np.array([ux, sx])
@njit
def ymotion(v, t):
    """
    :param v: initial velocity [m/s]
    :param t: Time [s]
    :return: Velocity in y direction [m/s], Position in y direction [m]
    """
    uy = np.round(v * np.sin(theta) - g * t, 1)
    sy = np.round(uy * t, 1) + 1.8  # throw height of 1.7m
    return np.array([uy, sy])
@njit
def zmotion(v, t):
    """
    :param v: initial velocity [m/s]
    :param t: Time [s]
    :return: Velocity in y direction [m/s], Position in Z direction [m]
    """
    vz = np.round(v * np.cos(phi) * t, 1)
    sz = np.round(vz * t, 1)
    return np.array([vz, sz])
print('Motion functions set up')
time = np.zeros(int(t_ui / dt))
velx = np.zeros(int(t_ui / dt))
vely = np.zeros(int(t_ui / dt))
velz = np.zeros(int(t_ui / dt))
disx = np.zeros(int(t_ui / dt))
disy = np.zeros(int(t_ui / dt))
disz = np.zeros(int(t_ui / dt))
print('arrays set up')
# initial conditions
velx[0] = veli
vely[0] = veli * np.sin(theta)
velz[0] = veli * np.cos(phi)
print('inital conditions set up')
for a in range(len(time) - 1):
    if disx[a] != x_ui:
        [velx[a + 1], disx[a + 1]] = xmotion(veli, time[a])
    else:
        pass
    if disy[a] != y_ui:
        [vely[a + 1], disy[a + 1]] = ymotion(veli, time[a])
    else:
        pass
    if disz[a] != z_ui:
        [velz[a + 1], disz[a + 1]] = zmotion(veli, time[a])
    else:
        pass
    time[a + 1] = time[a] + dt
    print('timestep calculated')
print('plotting')
ax = plt.axes(projection='3d')
ax.plot(disx, disy, disz, label='projectile')
ax.scatter(x_ui, y_ui, z_ui, label='target')
plt.legend(loc='best')
plt.show()
