# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 12:40:20 2021

@author: nobrien
"""

import random #import random module
import operator #import operator module
import matplotlib.pyplot #import module to plot graphs
import time #import time module 
import agentframework

start = time.time() # start of time to run code time

def distance_between(agents_row_a, agents_row_b):
    '''function to calculate distance between 2 agents,called agents_row_a and agents_row_b, each agent is a list with 2 values'''
    return(((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5

#creating and checking the class Agent
a = agentframework.Agent() #creating one instance of the class Agent from agentframework.py
print('creating one instance of the class Agent a')
print(a.y, a.x) #printing the attributes of the agent a


a.move() #moving the agent a by one 
print('moving a by one')
print(a.y, a.x)#printing the attributes of the agent a

print('print a') 
print(a) # printing agent a as defined in the agent class

  
num_of_agents=10 #number of agents 
num_of_iterations=100 #number of iterations for agents to be moved

#create an empty list for the agents
agents=[]

#add number of instants of Agent class to the agents list 
for i in range(num_of_agents):
    agents.append(agentframework.Agent())


##move each agent in the agents list 100 times
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        #method for moving an instant of Agent class, each agent in the list is moved 
        agents[i].move()


#create a graph plot of the points
matplotlib.pyplot.ylim(0, 99) #y axis limits
matplotlib.pyplot.xlim(0, 99) #x axis limits
for i in range(num_of_agents):
    #scatter plot all co-ordaintes x,y, for all agents, using the attributes of each agent
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y) 
matplotlib.pyplot.show()

#calculate the distance between each agent
for agents_row_a in agents: #for each one of the Agents in the agents list
    for agents_row_b in agents: #for each one of the Agents in the agents list
        distance = distance_between(agents_row_a, agents_row_b) #function that calculates the distance between each agent 
        #print(distance)
 

agent_list = []  #making a new empty list

# creates a list of the agent class coordinates
for i in range(num_of_agents):
   agent_list.append(agents[i].get()) # creates a list of the agent class coordinates, getting out the attributes   
 

print(agent_list)    
    
end = time.time() # time at end of code

print("time = " + str (end-start)) #prints the time taken to run the code


