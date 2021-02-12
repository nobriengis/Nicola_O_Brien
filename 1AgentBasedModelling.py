# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 12:40:20 2021


@author: nobrien
"""

import random


#set up variables y0 and x0 to be random integers between 0 and 99
y0=random.randint(0,99)
x0=random.randint(0,99)

print(y0,x0)

#use if statement to move y one step
if random.random() < 0.5:
    y0=y0+1
else:
    y0=y0-1


#use if statement to move x one step
if random.random() < 0.5:
    x0=x0+1
else:
    x0=x0-1

print(y0,x0)

#use if statement to move y another one step
if random.random() < 0.5:
    y0=y0+1
else:
    y0=y0-1


#use if statement to move x another one step
if random.random() < 0.5:
    x0=x0+1
else:
    x0=x0-1

print(y0,x0)


#set up variables y1 and x1 to be random intergers between 0 and 99
y1=random.randint(0,99)
x1=random.randint(0,99)

print(y1,x1)

#use if statement to move y one step
if random.random() < 0.5:
    y1+=1
else:
    y1-=1
   

#use if statement to move x one step
if random.random() < 0.5:
    x1+=1
else:
    x1-=1  

print(y1,x1)

#use if statement to move y another one step
if random.random() < 0.5:
    y1+=1
else:
    y1-=1
    

#use if statement to move x another one step
if random.random() < 0.5:
    x1+=1
else:
    x1-=1
    

print(y1,x1)

#Calculate the distance between the 2 agents (y0,x0) and (y1,x1)

dist=(((y1-y0)**2) + ((x1-x0)**2))**0.5

print(dist)
