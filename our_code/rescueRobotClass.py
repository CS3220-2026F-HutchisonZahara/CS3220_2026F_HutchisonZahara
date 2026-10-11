from src.mazeProblemSolvingAgentSMARTClass import MazeProblemSolvingAgentSMART
from our_code.labProblemClass import LabProblem

class RescueRobotAgent(MazeProblemSolvingAgentSMART):
  def __init__(self, initial_state=None, dataGraph=None, goal=None, labPaths=None, program=None, name="RescueRobot"):
    super().__init__(initial_state, dataGraph, goal, program)
    self.labPaths = labPaths
    self.name = name
    self.knownDrones = {}
    self.pathCost = None

  def formulate_problem(self, state, goal):
    return LabProblem(state, goal, self.dataGraph, self.labPaths)

  def search(self, problem):
    seq = self.program(problem)
    if seq is None:
      print("{}: no path to the rescue target. Mission failed.".format(self.name))
      self.alive = False
      return []
    self.pathCost = seq.path_cost
    solution = self.actions_path(seq.path())
    print("{}: solution {} with path cost {}".format(self.name, solution, self.pathCost))
    return solution

  def __repr__(self):
    return "<{} at {} energy={}>".format(self.name, self.state, round(self.performance, 2))
