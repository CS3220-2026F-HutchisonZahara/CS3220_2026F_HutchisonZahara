import random
from src.environmentProClass import environmentPro
from src.thingClass import Thing
from src.locations import *

from src.catFriendlyHouse_membersClass import Milk,Sausage,Mouse


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
    
    








  

