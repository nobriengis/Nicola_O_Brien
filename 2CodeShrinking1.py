# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 12:40:20 2021

@author: nobrien
"""

import random #import random module
import operator #import operator module
import matplotlib.pyplot #import module to plot graphs

#create an empty list for the agents
agents=[]


#append co-ordinates y0 and x0 (2 random integers) to the list
agents.append([random.randint(0,99),random.randint(0,99)])

#print(agents)

#print (agents[0][0], agents [0][1])


#use if statement to move y one step
if random.random() < 0.5:
    agents[0][0]+=1
else:
    agents[0][0]-=1


#use if statement to move x one step
if random.random() < 0.5:
    agents[0][1]+=1
else:
    agents[0][1]+=1

#print (agents[0][0], agents [0][1])


#use if statement to move y another one step
if random.random() < 0.5:
    agents[0][0]+=1
else:
    agents[0][0]-=1


#use if statement to move x another one step
if random.random() < 0.5:
    agents[0][1]+=1
else:
    agents[0][1]+=1



#append another set of coordinates, co-ordinates y1 and x1 (2 random integers) to the list
agents.append([random.randint(0,99),random.randint(0,99)])


#use if statement to move y1 one step
if random.random() < 0.5:
    agents[1][0]+=1
else:
    agents[1][0]-=1
   

#use if statement to move x1 one step
if random.random() < 0.5:
    agents[1][1]+=1
else:
    agents[1][1]-=1  


#use if statement to move y1 another one step
if random.random() < 0.5:
    agents[1][0]+=1
else:
    agents[1][0]-=1
    

#use if statement to move x1 another one step
if random.random() < 0.5:
    agents[1][1]+=1
else:
    agents[1][1]-=1
    
#print(agents[1])

print(agents)

#Calculate the distance between the 2 agents (y0,x0) and (y1,x1), i.e. betwemm agents[0] and agents[1]
dist=(((agents[1][0]-agents[0][0])**2) + ((agents[1][1]-agents[0][1])**2))**0.5

print(dist)

#print(max(agents)) #largest of the agents

#print(max(agents, key=operator.itemgetter(1)))#largest in the East/X (2nd element)

#create a graph plot of the points using matplotlib
matplotlib.pyplot.ylim(0, 99) #y-axis limits
matplotlib.pyplot.xlim(0, 99) #x-axis limits
matplotlib.pyplot.scatter(agents[0][1],agents[0][0]) #plot x0,y0
matplotlib.pyplot.scatter(agents[1][1],agents[1][0]) #plot x1,y1
#plot most easterly point in red
matplotlib.pyplot.scatter(max(agents, key=operator.itemgetter(1))[1],max(agents, key=operator.itemgetter(1))[0], color='red') 
matplotlib.pyplot.show() #show the plot
