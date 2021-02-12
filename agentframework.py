# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 17:53:00 2021

@author: nobrien
"""
import random

class Agent():
    #creating the class Agent, with two attributes y and x, both random integers between 0 and 99
    def __init__(self, y = 0, x = 0):
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)


    def __str__(self):
        #what happens when using print()
        return f'y = {self.y}, x= {self.x}'


    def move(self):
        #moves the pair of co-ordinates by one 
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
        
        #move x one step, for each x
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100

    
    def get(self):
        #returns a list of the attributes
        return [self.y, self.x]
    