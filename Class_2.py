#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 13:40:29 2018

@author: SadieCoffin
"""

# function for finding the slope and intercept of the line given x and y
def find_mb(x,y):
    N = float(len(x))
    sumx = sum(x[i] for i in range(len(x)))
    sumy = sum(y[i] for i in range(len(x)))
    sumxy = sum(x[i] * y[i] for i in range(len(x)))
    sumx2 = sum(x[i]**2 for i in range(len(x)))
    # use given definitions of m and b in terms of the x and y summations
    m = (N*sumxy - sumx*sumy) / (N*sumx2 - (sumx)**2)
    b = (sumy*sumx2 - sumx*sumxy) / (N*sumx2 - (sumx)**2)
    return m,b
    
# alternative method for finding slope and intercept
def find_mb2(x,y):
    N = float(len(x))
    sumx=0
    sumy=0
    sumxy=0
    sumx2=0
    for i in range(len(x)):
        sumx += x[i]
        sumy += y[i]
        sumxy += x[i]*y[i]
        sumx2 += x[i]**2
    m = (N*sumxy - sumx*sumy) / (N*sumx2 - (sumx)**2)
    b = (sumy*sumx2 - sumx*sumxy) / (N*sumx2 - (sumx)**2)
    return m,b
        


# say you have columns of data, eg in example file data.csv
def datacols_to_list(file):
    x = [ ]
    y = [ ]
    r = [ ]
    for line in open(file, 'r').readlines():
        if 'logP' in line:
            continue
        vals = line.strip().split(',')
        # read in x, y, and r values
        x += [float(vals[0])]
        y += [float(vals[1])]
        r += [float(vals[2])]
    return x, y, r
    
import matplotlib.pyplot as plt

def create_plot(x,y):
    m,b = find_mb(x,y)
    mx = [float(i) for i in range(50)]
    my = [m*xi + b for xi in mx]
    kwargs = {'mfc':'white','mec':'crimson','linestyle':'none','marker':'.','label':'Data'}
    mkwargs = {'color':'black','linestyle':'--', 'label':'Model'}
    plt.plot(x, y, **kwargs)
    plt.plot(mx, my, **mkwargs)
    plt.xlabel('logP')
    plt.ylabel('Mw')
    plt.xlim(0, 1.9)
    plt.ylim(-3, -9)
    plt.legend()
    #plt.show()
    plt.savefig('plotting')
    plt.close()
    
    
    
    
    
    
    