#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 13:40:05 2018

@author: SadieCoffin
"""

def sqrt(N):
    x = (1/2) * N
    for i in range(10): 
        x = (1/2) * (x + N/x)
    return x

x = 52
y = "Hello"
z = [1, 2, 3]

# square root function using for loop
def sqrt2(N,niter=100):
    xn = N/2. # starting guess
    for n in range(niter):
       xn = 0.5*(xn+N/xn) # update x_n to x_n+1
       if xn**2. == N:
           break # interrupt iteration if solution is found
    return xn

# square root function using while loop
def sqrt3(N,niter=100):
    xn = N/2.
    n = 0 # this is the counter for the number of iterations!
    while xn**2. != N and n < niter:
       xn = 0.5*(xn+N/xn) # update x_n to x_n+1
       n += 1 # updating the counter for the next iteration
    return xn

def precess(ra, dec, nyears=1):
    for n in range(nyears):
        dra = 3.0748+1.3361*sin(ra*pi/180)*tan(dec*pi/180)
        ddec = 20.042*cos(ra*pi/180)
        if ra > 360:
            ra = ra - 360
    return ra+dra*(15/3600), dec+ddec/3600