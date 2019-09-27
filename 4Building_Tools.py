# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:21:11 2019

@author: nobrien
"""
import random
import operator
import matplotlib.pyplot
import time

start = time.perf_counter()

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

num_of_agents = 100
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
     agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        if random.random() < 0.5:
             agents[i][0] = (agents[i][0] + 1) % 100
        else:
             agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
             agents[i][1] = (agents[i][1] + 1) % 100
        else:
             agents[i][1] = (agents[i][1] - 1) % 100
        

answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer)


matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()        

distance = distance_between(agents[0], agents[1])

print(distance)



# The code to run, here.

end = time.perf_counter()

print("time = " + str(end - start))