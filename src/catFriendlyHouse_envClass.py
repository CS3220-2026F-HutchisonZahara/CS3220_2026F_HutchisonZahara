import random
from src.environmentProClass import environmentPro
from src.thingClass import Thing
from src.locations import *

from src.catFriendlyHouse_membersClass import Milk,Sausage,Mouse

from src.agentClass import Agent, proCatAgent


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
    
  

  def percept(self, agent):
    #return a list of things that are in our agent's location
    things = self.list_things_at(agent.location)
    return agent.location, things
    
  def execute_action(self, agent, action):
    #changes the state of the environment based on what the agent does.
    if self.is_agent_alive(agent):
      #the current agent is Cat & Mouse is still there
      if isinstance(agent, proCatAgent) and len(self.)>0:
        print("Both agents are still ")
        if action=='Go ahead':
          if agent.direction==True:
            agent.location=self.locations[self.locations.index(agent.location)+1]
          else:
            agent.location=self.locations[self.locations.index(agent.location)+1]
          agent.performance -= 5
          self.update_agent_alive(agent)
          print("The Agent decided to {} at location: {}".format(action,agent.location))

        elif action=='Catch':
          items = self.list_things_at(agent.location, thingClass=Agent)
          if agent.performance>items[0].performance*5:
            #a cat caught a mouse
            self.delete_thing(items[0])
            agent.performance += 10
            self.update_agent_alive(agent)
            print("The Agent did {} {} at location: {}".format(action,items[0],agent.location))

          else:
            #a cat tried but a mouse run away
            agent.performance -= 10
            self.update_agent_alive(agent)
            print("The Agent tried to {} {} at location: {}, but failed.".format(action,items[0],agent.location))

        elif action=='Change direction':
          agent.changeDirection()

      elif isinstance(agent, Agent):
        print("the Agent Mouse is still running")
        agent.location=action
        print("The Agent Mouse decided to move to {}".format(agent.location))        
        agent.performance -= 1
        self.update_agent_alive(agent)

      else:
          print("There is nothing for Agent Cat here. Done!")
          agent.alive=False
    
    
  def is_done(self):
    no_agents = not any(agent.is_alive() for agent in self.agents)
    #return no_agents or no_items
    return no_agents
    
    








  

