from src.navigationEnvironmentClass import MazeNavigationEnvironment

class LabEnvironment(MazeNavigationEnvironment):
  def __init__(self, navGraph, maze, drones, labPaths):
    super().__init__(navGraph)
    self.maze = maze
    self.paths = labPaths
    self.drones = {drone.location: drone for drone in drones}

  def execute_action(self, agent, action):
    if self.is_agent_alive(agent):
      path = self.paths[(agent.state, action)]
      agent.performance -= 1
      for cell in path:
        agent.state = cell
        self.drone_encounter(agent)
        if not agent.alive:
          return
      print(f"{agent.name} in {agent.state} with performance = {round(agent.performance, 2)}")
      self.update_agent_alive(agent)

  def drone_encounter(self, agent):
    drone = self.drones.get(agent.state)
    if drone is None:
      return
    agent.knownDrones[drone.location] = drone.attack_power
    print(f"{agent.name} met a security drone at {drone.location} with attack power {drone.attack_power}")

    if drone.attack_power >= 2 * agent.performance:
      agent.alive = False
      print(f"The drone captured {agent.name}. {agent} is dead.")
    else:
      agent.performance -= 0.10 * agent.performance
      print(f"{agent.name}: Defense Mode activated! Energy is now {round(agent.performance, 2)}")
