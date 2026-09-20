import random
from src.environmentProClass import environmentPro
from src.thingClass import Thing
from src.locations import *

from src.catFriendlyHouse_membersClass import Milk,Sausage,Mouse

from src.agentClass import Agent, proCatAgent, MouseAgent


#catFriendlyHouse_envClass
class catFriendlyHouse_env(environmentPro):
  def __init__(self):
    super().__init__()
    self.locations=[loc_A, loc_B, loc_C]

  def default_location(self, thing):
    print("The item is starting in random location...")
    return random.choice(self.locations)
  
    
  

  def percept(self, agent):
    #return a list of things that are in our agent's location
    #your code here
    pass
    
  def execute_action(self, agent, action):
    #changes the state of the environment based on what the agent does.
    #your code here
    pass
    
  def is_done(self):
    #your code here
    pass



  #catFriendlyHouse_envClass
class catFriendlyHouse2_env(environmentPro):
  def __init__(self):
    super().__init__()
    self.locations=[loc_A, loc_B, loc_C, loc_D]

  def default_location(self, thing):
    print("The item is starting in random location...")
    return random.choice(self.locations)
  
  #Return all things exactly at a given location
  def list_agents_at(self, location, thingClass=Thing):
    return [agent for agent in self.agents if agent.location == location and isinstance(agent, thingClass)]
    
  

  def percept(self, agent):
    #return a list of things AND a list of agents that are in our agent's location
    #Cat Agent program must be updated to process 3 items from its perception
    things = self.list_things_at(agent.location)
    agents = self.list_agents_at(agent.location)
    return agent.location, things, agents
  

  def add_thing(self, thing, location=None): # improved  
    # perf = original one not 0 like in parent class
    #from src.agentClass import Agent
    if thing in self.agents:
      print("Can't add the same agent twice")
    else:
      if isinstance(thing, Agent):
        #thing.performance = 0
        thing.location = location if location is not None else self.default_location(thing)
        self.agents.append(thing)
        print(f"Welcome! You are added in location {thing.location}")
    if thing in self.things and thing.location==location:
      print("Can't add the same agent twice")
    else:
      if not isinstance(thing, Agent):
        thing.location = location if location is not None else self.default_location(thing)
        self.things.append(thing)
    
  def execute_action(self, agent, action):
    #changes the state of the environment based on what the agent does.
    if self.is_agent_alive(agent):
      #the current agent is Cat & Mouse is still there
      if isinstance(agent, proCatAgent) and len(self.agents+self.things)>0:
        print("Some items are still there ....")
        if action=='Go ahead':
          print("The Agent decided to {} at location: {}".format(action,agent.location))
          if agent.direction==True:
            agent.location=self.locations[self.locations.index(agent.location)+1]
          else:
            agent.location=self.locations[self.locations.index(agent.location)-1]
          agent.performance -= 5
          self.update_agent_alive(agent)
          

        elif action=='Catch':
          items = self.list_agents_at(agent.location, thingClass=MouseAgent)
          if items: 
            target_mouse = items[0]
            if agent.performance>target_mouse.performance*5:
              #a cat caught a mouse -> remove Mouse Agent form agents list
              self.delete_thing(target_mouse)
              agent.performance += 10
              self.update_agent_alive(agent)
              print("The Agent did {} {} at location: {}".format(action,target_mouse,agent.location))
              print("There is nothing for Agent Cat here. Done!")
              agent.alive=False

            else:
              #a cat tried but a mouse run away
              agent.performance -= 10
              self.update_agent_alive(agent)
              print("The Agent tried to {} {} at location: {}, but failed.".format(action,items[0],agent.location))
          else:
            print(f"Agent tried to {action}, but no MouseAgent was found at {agent.location}.")
        
        elif action=='Check direction':
          print("The Agent decided to {} at location: {}".format(action,agent.location))
          if agent.location==loc_A and not agent.direction:
            agent.changeDirection()

          if agent.location==loc_D and agent.direction:
            agent.changeDirection()
          
          #print(agent.direction)
          if agent.direction==True:
            agent.location=self.locations[self.locations.index(agent.location)+1]
          else:
            agent.location=self.locations[self.locations.index(agent.location)-1]
          agent.performance -= 5
          self.update_agent_alive(agent)

        elif action=='Stop':
          print("There is nothing for Agent Cat here. Done!")
          agent.alive=False
          

      elif isinstance(agent, MouseAgent):
        print(f"the Agent Mouse is still running with a performance {agent.performance}")
        agent.location=action
        print("The Agent Mouse decided to move to {}".format(agent.location))
        #items = self.list_agents_at(agent.location, thingClass=MouseAgent)
        #self.delete_thing(items[0])
        agent.performance -= 1
        self.update_agent_alive(agent)
        #self.add_thing(agent,agent.location)
        #print(self.agents)

      else:
          print("There is nothing for Agent Cat here. Done!")
          agent.alive=False
    
    
  def is_done(self):
    no_agents = not any(agent.is_alive() for agent in self.agents)
    #return no_agents or no_items
    return no_agents
    
    








  

