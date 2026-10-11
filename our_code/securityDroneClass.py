import random
from src.thingClass import Thing

class SecurityDrone(Thing):
  def __init__(self, location, numNodes):
    self.location = location
    self.attack_power = round(random.uniform(0.10, 0.40) * numNodes, 2)

  def __repr__(self):
    return "<SecurityDrone at {} attack={}>".format(self.location, self.attack_power)
