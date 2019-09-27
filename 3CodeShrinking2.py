# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:40:20 2019

@author: nobrien
"""
import random

'''agents = [] 

#random y0, x0 between 0 and 99, and append to end of the list agents

y0 = random.randint (0,99)
x0 = random.randint (0,99)

agents.append ([y0, x0])

#random y1, x1 between 0 and 99, and append to end of the list agents

y1 = random.randint (0,99)
x1 = random.randint (0,99)

agents.append ([y1, x1])

# print (agents)'''

import operator 

import matplotlib.pyplot

num_of_agents = 10

agents = []  #make new empty list 

#creates 10 sets of co-ordinates

'''for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

 
#random y0, x0 between 0 and 99, and append to end of the list agents and 
#random y1, x1 between 0 and 99, and append to end of the list agents   
#agents.append([random.randint(0,99),random.randint(0,99)])
#agents.append([random.randint(0,99),random.randint(0,99)])

print (agents)

#print(max(agents))

#print(max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.show()'''

'''if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1

if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1'''

#for i in range (num_of_agents):

'''if random.random() < 0.5:
    agents[i][0] += 1
else:
    agents[i][0] -= 1
    
agents.append ([y1, x1])
    
print(agents)  '''  
    
for i in range(num_of_agents):
    agents([random.randint(0,99),random.randint(0,99)])

print(agents)