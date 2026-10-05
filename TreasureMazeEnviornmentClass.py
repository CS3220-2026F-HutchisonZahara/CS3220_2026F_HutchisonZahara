from src.environmentClass import Environment
from src.graphClass import Graph

class TreasureMazeEnviornment(Environment):
  def __init__(self, graph: Graph, treasure_locations: dict):
    super().__init__()
    self.graph = graph
    self.treasureLocations = treasure_locations

  def add_thing(self, thing, location=None):
    if thing in self.agents:
      print("Can't add the same agent twice")
      return
    thing.performance = len(self.graph.nodes()) // 2
    thing.collected = []
    self.agents.append(thing)
    thing(thing.state)
    print(f'Agent at {thing.state} with performance {thing.performance}')
    print(f'Plan: {thing.seq}')

  def execute_action(self, agent, action):
    agent.state = action
    agent.performance -= 1
    print(f'Agent moved to {agent.state}, performance = {agent.performance}')
    if agent.state in self.treasureLocations:
      treasure = self.treasureLocations.pop(agent.state)
      agent.collected.append(treasure)
      print(f'Agent grabbed {treasure}!')

  def step(self):
    actions = []
    if self.is_done():
      print("There is no one here who could work...")
      return actions
    for agent in self.agents:
      if not agent.alive:
        continue
      action = agent.seq.pop(0)
      actions.append(action)
      self.execute_action(agent, action)
      if not agent.seq:
        print(f'Agent reached the exit with {agent.collected}')
        agent.alive = False
      elif agent.performance <= 0:
        print('Agent ran out of performance and died')
        agent.alive = False
    return actions

  def is_done(self):
    return not any(agent.alive for agent in self.agents)

  def is_agent_alive(self, agent):
    return agent.alive

  def run(self, steps=50):
    step = 0
    while not self.is_done() and step < steps:
      step += 1
      print(f'step {step}:')
      self.step()
