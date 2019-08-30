# imports
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# user input
# make a check so user can only input integers
print('Target Coordinates')
x_ui = float(input('Input x co-ordinate [m]\n'))
if x_ui == 0:
    x_ui = 0.001
y_ui = float(input('Input y co-ordinate [m]\n'))
if y_ui == 0:
    y_ui = 0.001
t_ui = float(input("Input time of flight [s]\n"))
if t_ui == 0:
    t_ui = 0.001
# define inital conditions
g = 9.8  # acceleration due to gravity [m/s^2]
dt = 0.01  # timestep [s]
phi = np.arctan(y_ui / x_ui)
def vel(x, y, t, a, b):
    v = 0
    return v
veli = vel(x_ui, y_ui, t_ui, phi)
print('Veloticy = ', veli)
def xmotion(v, t):
    """
    :param v: initial velocity [m/s]
    :param t: Time [s]
    :return: Velocity in x direction [m/s], position in x direction [m]
    """
    ux = np.round(v * t, 1)
    sx = np.round(ux * t, 1)
    return np.array([ux, sx])
def ymotion(v, t):
    """
    :param v: initial velocity [m/s]
    :param t: Time [s]
    :return: Velocity in y direction [m/s], Position in y direction [m]
    """
    uy = np.round(v * np.sin(phi) - g * t, 1)
    sy = np.round(uy * t, 1) + 1.8  # throw height of 1.7m
    return np.array([uy, sy])