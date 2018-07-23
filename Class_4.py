#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 13:32:36 2018

@author: SadieCoffin
"""

# definite integrals


# function that does simpsons rule and returns parabolic approximate integral
def simpsons_rule(a, b, f):
    """Given function and integral limits a and b, returns parabolic approximate
    integral
    """
    approx_integral = ((b - a)/6) * (f(a) + 4*f((a+b)/2) + f(b))
    return approx_integral

# constants:
omega_m = 0.27
omega_lambda = 0.73
omega_k = 0
H_0 = 73.5 #km/s/Mpc
c = 3e-5 #m/s

from math import sqrt

def E(z):
    return (1/sqrt(((1+z)**3)*0.27 + ((1+z)**2)*0 + 0.73))

def d_c(a=0, b=10e-3):
    return simpsons_rule(a, b, E)

def d_approx(z):
    return (z*c)/H_0

import numpy as np
import matplotlib.pyplot as plt


dc_values = []
z = 10**(np.linspace(-3, 1, 100))
for i in range(len(z)):
    dc_values.append(d_c(b=z[i]))
dist_values = dc_values
# print(dist_values)

def plot_lin():
    plt.plot(z, dist_values)
    plt.plot(z, z)

# plot log scale of z (redshift) vs. the 2 ways of measuring distance
# this plot tells us that the 2 measurment methods diverge around z=0.2
def plot_log():
    plt.loglog(z, dist_values)
    plt.loglog(z, z)
    











