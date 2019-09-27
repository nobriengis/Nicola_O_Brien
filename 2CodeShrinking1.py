# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:40:20 2019

@author: nobrien
"""
import random

agents = []

#random number between 0 and 99

y0 = random.randint(0,99)
x0 = random.randint(0,99)


# Random walk one step

if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

print(y0, x0)

agents.append ([y0, x0])

print (agents)

# set up variables

y1 = random.randint(0,99)
x1 = random.randint(0,99)

# Random walk one step

if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1
    
print(y1, x1)

y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq
answer = sum**0.5
print(answer)