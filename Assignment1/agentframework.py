
"""
——————Version 1.0.0——————
This is a basic Agent class, every agent is located in a 2D plane and represented
by a raster environment. This class also includes functions about agents' behaviour
and thire interactions with each other agent. 
@author: FUGANGZHOU
"""

import random as r

class Agent:
    '''
    Initialises an agent.
    Postional arguments:
    environment —— the raster environment to be shared with all agents.
    agents —— a reference to all agents in environment.
    '''
    def __init__(self,environment,agents,x,y):
        self.environment = environment
        self.store = 0
        self.agents = agents
        #self.x = r.randint(0,300)
        #self.y = r.randint(0,300)
        if (x == None):
            self.x = r.randint(0,300)
        else:
            self.x = x
        if (y == None):
            self.y = r.randint(0,300)
        else:
            self.y = y
        
    '''
    Move the agent.
    Make the agent move randomly in the environment and return its coordinate value.
    The agent will come out from the opposite boundary when it reaches the boundary line.
    ''' 
    def move(self):
        '''Returns: Return the coordinates of agent.'''
        if r.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300

        if r.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300
        return (self.x, self.y)
    '''
    Agent removes(eat) some of the environment
    '''
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
    '''
    Calculate and return the distance between self and agent.
    Postional arguments:
    agent —— an instance of this Agent class
    '''        
    def distance_between(self,agent):
        '''Returns: Return the distance between self and agent'''
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    '''
    Agents share the store with their neighbours.
    Postional arguments:
    neighbourhood —— the distance within which agents share with their neighbours.
    '''
    def share_with_neighbourhoods(self,neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent)
            if not distance > neighbourhood:
                sum = self.store + agent.store
                ave = sum/2
                self.store = ave
                agent.store = ave
                #print('sharing'+str(distance)+' '+str())
                
    