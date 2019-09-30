# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:50:16 2019

@author: nobrien
"""

import csv
import matplotlib.pyplot

'''f = open('in.txt', newline='')		
for line in f:
	print(line)
f.close()'''

f = open('in.txt')

dataset = csv.reader (f, quoting=csv.QUOTE_NONNUMERIC)

environment = []

num_of_agents = 10
num_of_iterations = 100

for row in dataset:
    rowlist=[]
    for value in row:
        rowlist=[rowlist.append(value)]
    environment=[environment.append(rowlist)]

matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

agents.append(agentframework.Agent(environment))

def __init__(environment):
    self.environment = environment
    self.store = 0
    
    
def eat(self): # can you make it eat what is left?
    if self.environment[self.y][self.x] > 10:
        self.environment[self.y][self.x] -= 10
        self.store += 10
        
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()       




