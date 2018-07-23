#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 13:35:08 2018

@author: SadieCoffin
"""


# root finding methods: bracket method

def f(x):
    f = x**2 + 2*x + 1
    return f

def bracket(delx, x0, x1):
    x_lower = x0
    x_upper = x0 + delx
    while x_upper < x1 and f(x_lower)*f(x_upper) > 0:
        x_lower += delx
        x_upper += delx
    return (x_lower + x_upper) / 2


# root finding methods: bissection method
def bisect(x_min, x_max, f, tol):
    x_lower = x_min
    x_upper = x_max
    x_mid = (x_min + x_max) / 2
    # take abs value bc if x_upper and x_lower both <0 this will be negative
    while abs(x_upper - x_lower) > tol:
        #if sign change happens in lower half, redefine upper limit to be the midpoint
        if f(x_lower)*f(x_mid) < 0:
            x_upper = x_mid
        elif f(x_upper)*f(x_mid) < 0:
            x_lower = x_mid
        # update x_mid to the new x_lower and x_upper
        x_mid = (x_lower + x_upper) / 2
    return x_mid
    
# try bissection method with science function R(T) - we want to find T, so use
    # some observed value of R and try and find where the difference between 
    # R(T) and R_observed is minimized/0
from math import exp
    
def R(T):
    R = (7.869 / (1 + 4.371 * T**(-.5))) * exp(3.3975/T)
    difference = 20 - R
    return difference



# root finding methods: newton raphson method
def dfdx(x, f):
    h = 1e-6 * x # want h << x 
    return (f(x+h) - f(x)) / h

def newt_raph(x_old, f, tol, P):
    # define g as the function f(x) with dependent variable x and fixed arguments
    # *P, which refers to the list of parameters given when calling the function, 
    # (in the place of argument) ---in this case, P is a list of 2 elements which
    # gives values for e and M, the second 2 variables in kepler's law
    g = lambda x:f(x, *P)
    x_new = x_old - (g(x_old) / dfdx(x_old, g))
    while abs(g(x_old) - g(x_new)) > tol:
        x_old = x_new
        x_new = x_old - (g(x_old) / dfdx(x_old, g))
    # the returned value of x_new, the root, gives us a value for E, the angle
    # that gets passed into kepler's laws to find x = r(cosE - e) and y = rsinE
    return x_new

from math import sin

# kepler's equation
def func(E, e, M):
    return E - e*sin(E) - M



