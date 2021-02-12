# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 12:40:20 2021

@author: nobrien
"""

import random #import random module
import operator #import operator module
import matplotlib.pyplot #import module to plot graphs

num_of_agents=10 #number of agents 
num_of_iterations=100 #number of iterations for age

#create an empty list for the agents
agents=[]

#create number of agents, all appended to list agents
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

#print(agents)  

#move each agent in the agents list 100 times
for j in range(num_of_iterations):#repeat inner loop 100 times
    #move each agent once using agents[i]
    for i in range(num_of_agents):
        #move y one step, for each y, taking the boundaray effect into account
        if random.random() < 0.5:
            agents[i][0]=(agents[i][0]+1)%100 #takes boundary into account
        else:
            agents[i][0]=(agents[i][0]-1)%100
        
        #move x one step, for each x, taking the boundaray effect into account
        if random.random() < 0.5:
            agents[i][1]=(agents[i][1]+1)%100
        else:
            agents[i][1]=(agents[i][1]-1)%100
    

print(agents)


#create a graph plot of the points using matplotlib
matplotlib.pyplot.ylim(0, 99) #y-axis limits
matplotlib.pyplot.xlim(0, 99) #x-axis limits
for i in range(num_of_agents):
    #scatter plot all co-ordaintes x,y, for all agents
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
#plot most easterly point in red
#matplotlib.pyplot.scatter(max(agents, key=operator.itemgetter(1))[1],max(agents, key=operator.itemgetter(1))[0], color='red') 
matplotlib.pyplot.show()
