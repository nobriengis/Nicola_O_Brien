# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:09:20 2019

@author: nobrien
"""

        
        
def share_with_neighbours(self, neighbourhood):
    for agent in self.agents:
        dist = self.distance_between(agent)
        if dist <= neighbourhood:
            sum = self.store + agent.store
            ave = sum /2
            self.store = ave
            agent.store = ave
            print("sharing " + str(dist) + " " + str(ave))

def distance_between(self, agent):
    return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5

for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)