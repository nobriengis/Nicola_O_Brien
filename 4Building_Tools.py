# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 12:40:20 2021

@author: nobrien
"""

import random #import random module
import operator #import operator module
import matplotlib.pyplot #import module to plot graphs
import time #import time module 

start = time.time() # start of time to run code time

def distance_between(agents_row_a, agents_row_b):
    '''function to calculate distance between 2 agents,called agents_row_a and agents_row_b, each agent is a list with 2 values'''
    return((((agents_row_a[0] - agents_row_b[0]) **2) + ((agents_row_a[1] - agents_row_b[1]) **2))**0.5)

    
num_of_agents=10 #number of agents 
num_of_iterations=100 #number of iterations for age

#create an empty list for the agents
agents=[]

#append co-ordinates y0 and x0 (2 random integers) to the list
#agents.append([random.randint(0,99),random.randint(0,99)])

#print(agents)

#create number of agents, all appended to list agents
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

#print(agents)  

for j in range(num_of_iterations):#repeat inner loop 100 times
    #move each agent once using agents[i]
    for i in range(num_of_agents):
        #move y one step, for each y,taking the boundaray effect into account
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
        
        #move x one step, for each x,taking the boundaray effect into account
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
    

#run the function distance_between to calculate the distance between every agent
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        print(distance)
        

#create a graph plot of the points
matplotlib.pyplot.ylim(0, 99) #y axis limits
matplotlib.pyplot.xlim(0, 99) #x axis limits
for i in range(num_of_agents):
    #scatter plot all co-ordaintes x,y, for all agents
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()


end = time.time() # time at end of code

#prints the time taken to run the code
print("time = " + str (end-start)) 
