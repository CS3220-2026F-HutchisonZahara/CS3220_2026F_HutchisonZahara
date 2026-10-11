from src.mazeProblemClass import MazeProblem
from our_code.labMazeData import moves

actionCosts = {0: 2, 1: 4, 2: 2, 3: 1}

class LabProblem(MazeProblem):
  def __init__(self, initial, goal, graph, labPaths):
    super().__init__(initial, goal, graph)
    self.paths = labPaths

  def result(self, state, action):
    return self.graph.origin[state][action]

  def path_cost(self, cost_so_far, A, action, B):
    return cost_so_far + self.edge_cost(A, action)

  def edge_cost(self, A, action):
    cells = [A] + self.paths[(A, action)]
    cost = 0
    for (r1, c1), (r2, c2) in zip(cells, cells[1:]):
      step = [a for a, move in moves.items() if move == (r2 - r1, c2 - c1)][0]
      cost += actionCosts[step]
    return cost
