from agentClass import Agent
from navigationEnvironmentClass import MazeNavigationEnvironment
from thingClass import Thing


class SecurityDrone(Thing):
    def __init__(self, attackPower):
        super().__init__()
        self.attackPower = attackPower


class RescueRobot(Agent):
    def __init__(self, energy: int):
        super().__init__()
        self.performance = energy


class LaboratoryEnvironment(MazeNavigationEnvironment):
    def __init__(self, maze):
        super().__init__(maze)

    def execute_action(self, agent, action):
        if self.is_agent_alive(agent):
            """Change agent's location -> agent's state;
            Track performance.
            -1 for each move."""
            agent.state = agent.update_state(agent.state, action)
            agent.performance -= 1
            print(f"Agent in {agent.state} with performance = {agent.performance}")
            self.update_agent_alive(agent)

            if action == 'Right':
                agent.location = loc_B
                agent.performance -= 1
                self.update_agent_alive(agent)
            elif action == 'Left':
                agent.location = loc_A
                agent.performance -= 1
                self.update_agent_alive(agent)