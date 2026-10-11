from queue import PriorityQueue
from src.nodeClass import Node


def childNode(problem, node, action):
  nextState = problem.result(node.state, action)
  return Node(nextState, node, action, problem.path_cost(node.path_cost, node.state, action, nextState))


def expand(problem, node):
  return [childNode(problem, node, action) for action in problem.actions(node.state)]


def UniformCostSearchAgentProgram():

  def program(problem):
    node = Node(problem.initial)
    frontier = PriorityQueue()
    count = 0
    frontier.put((node.path_cost, count, node))
    reached = {problem.initial: node}

    while not frontier.empty():
      node = frontier.get()[2]
      if problem.goal_test(node.state):
        return node
      for child in expand(problem, node):
        if child.state not in reached or child.path_cost < reached[child.state].path_cost:
          reached[child.state] = child
          count += 1
          frontier.put((child.path_cost, count, child))
    return None

  return program


def IDSearchAgentProgram():

  def onPath(node, state):
    while node:
      if node.state == state:
        return True
      node = node.parent
    return False

  def recursiveDLS(node, problem, limit):
    if problem.goal_test(node.state):
      return node
    if node.depth == limit:
      return "cutoff"
    cutoffOccurred = False
    for successor in expand(problem, node):
      if onPath(node, successor.state):
        continue
      result = recursiveDLS(successor, problem, limit)
      if isinstance(result, Node):
        return result
      if result == "cutoff":
        cutoffOccurred = True
    return "cutoff" if cutoffOccurred else "failure"

  def depthLimitedSearch(problem, limit):
    return recursiveDLS(Node(problem.initial), problem, limit)

  def program(problem):
    depth = 0
    while True:
      print("Depth Limit = {}".format(depth))
      result = depthLimitedSearch(problem, depth)
      if result != "cutoff":
        return result if isinstance(result, Node) else None
      depth += 1

  return program
