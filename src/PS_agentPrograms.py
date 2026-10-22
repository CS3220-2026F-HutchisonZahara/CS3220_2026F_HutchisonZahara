#How do we decide which node from the frontier to expand next?
from src.nodeClass import Node
from queue import PriorityQueue

import math

nodeColors={
    "start":"red",
    "goal": "green",
    "frontier": "orange",
    "expanded":"pink"
}

# task 2
def manhat_dist(a: tuple[int, int], b: tuple[int, int]) -> int:
  return abs(a[0] - b[0]) + abs(a[1] - b[1])


def A_StarSearchAgentProgram(f=math.dist):  # task 1
  
    #f=math.dist
    
    def program(problem):
      # print("Hi")

      node = Node(problem.initial)
      counter = 0
 
      frontier = PriorityQueue()
      h=node.path_cost+round(f(node.state, problem.goal),3)
      frontier.put((h,node))
      reached = {problem.initial:node}

      while not frontier.empty():
        print(frontier.queue)
        node = frontier.get()[1]
        print("The node {} is extracted from frontier:".format(node.state))

        if problem.goal_test(node.state):
          print("We have found our goal: {}".format (node.state))
          print("Nodes expanded: {}".format(counter))
          print("Total path cost: {}".format(node.path_cost))
          node.expanded=counter
          return node

        #reached.add(node.state)
        counter += 1
        for child in node.expand(problem):
            if child.state not in reached or child.path_cost<reached[child.state].path_cost:
                #print(child)
                print("The child node {}.".format(child))
                h=child.path_cost+round(f(child.state, problem.goal),3)
                frontier.put((h,child))
                reached.update({child.state:child})
            
      return None

    return program



def IDA_StarSearchAgentProgram(f=math.dist):  # task 7

    def program(problem):
      counter = 0

      def fCost(node):
        return node.path_cost + f(node.state, problem.goal)

      def dfsContour(node, fLimit):
        nonlocal counter
        if fCost(node) > fLimit:
          return None, fCost(node)
        if problem.goal_test(node.state):
          return node, fLimit
        counter += 1
        nextF = math.inf
        onPath = [n.state for n in node.path()]
        for s in node.expand(problem):
          if s.state in onPath:  # no going back over the path (left/right cost 0)
            continue
          solution, newF = dfsContour(s, fLimit)
          if solution:
            return solution, fLimit
          nextF = min(nextF, newF)
        return None, nextF

      root = Node(problem.initial)
      fLimit = fCost(root)
      while True:
        solution, fLimit = dfsContour(root, fLimit)
        if solution:
          print("We have found our goal: {}".format(solution.state))
          print("Nodes expanded: {}".format(counter))
          print("Total path cost: {}".format(solution.path_cost))
          solution.expanded = counter
          return solution
        if fLimit == math.inf:
          return None

    return program


def RBFS_SearchAgentProgram(f=math.dist):  # task 8

    def program(problem):
      counter = 0

      def rbfs(node, fLimit):
        nonlocal counter
        if problem.goal_test(node.state):
          return node, node.f
        counter += 1
        onPath = [n.state for n in node.path()]
        successors = [s for s in node.expand(problem) if s.state not in onPath]  # no going back over the path
        if not successors:
          return None, math.inf
        for s in successors:
          s.f = max(s.path_cost + f(s.state, problem.goal), node.f)
        while True:
          successors.sort(key=lambda s: s.f)
          best = successors[0]
          if best.f > fLimit:
            return None, best.f
          alternative = successors[1].f if len(successors) > 1 else math.inf
          result, best.f = rbfs(best, min(fLimit, alternative))
          if result:
            return result, best.f

      root = Node(problem.initial)
      root.f = f(root.state, problem.goal)
      solution, fvalue = rbfs(root, math.inf)
      if solution:
        print("We have found our goal: {}".format(solution.state))
        print("Nodes expanded: {}".format(counter))
        print("Total path cost: {}".format(solution.path_cost))
        solution.expanded = counter
      return solution

    return program


def BestFirstSearchAgentProgram(f=None):
  #with BFS we choose a node, n, with minimum value of some evaluation function, f (n).
    
    def program(problem):

      node = Node(problem.initial)
      #node.color=nodeColors["start"]
      #print(node.state)
      frontier = PriorityQueue()
      frontier.put((1,node))
      print(f"The {node} is being pushed to frontier ...")
      #node.color=nodeColors["frontier"]
      reached = {problem.initial:node}

      while frontier:
        node = frontier.get()[1]
        #node.color=nodeColors["expanded"]
        print(f"The {node} is being extracted from frontier ...")

        if problem.goal_test(node.state):
          node.color=nodeColors["goal"]
          print(f"We have found our goal:  {node}!")
          return node

        #reached.add(node.state)
        for child in node.expand(problem):
            if child.state not in reached or child.path_cost<reached[child.state].path_cost:
                frontier.put((1,child))
                print(f"The child {child} is being pushed to frontier ...")
                #child.color=nodeColors["frontier"]
                reached.update({child.state:child})
            
        #node.color=nodeColors["expanded"]
      return None

    return program
  
 
# def IDSearchAgentProgram(f=None):
#   def program(problem):
#     #your code here
    
 
      











def BestFirstSearchAgentProgramForShow(f=None):
  #with BFS we choose a node, n, with minimum value of some evaluation function, f (n).
    
    def program(problem):
      #print(111)
      steps = 0
      allNodeColors = []
      nodeColors = {k : 'white' for k in problem.graph.nodes()}

      node = Node(problem.initial)
      nodeColors[node.state] = "yellow"
      steps += 1
      allNodeColors.append(dict(nodeColors))

      #print(node.state)
      frontier = PriorityQueue()
      frontier.put((1,node))

      nodeColors[node.state] = "orange"
      steps += 1
      allNodeColors.append(dict(nodeColors))



      reached = {problem.initial:node}

      while frontier:
        node = frontier.get()[1]
        nodeColors[node.state] = "red"
        steps += 1
        allNodeColors.append(dict(nodeColors))
        #print(node)

        if problem.goal_test(node.state):
          nodeColors[node.state] = "green"
          steps += 1
          allNodeColors.append(dict(nodeColors))
          return (node,steps,allNodeColors)
          

        #reached.add(node.state)
        for child in node.expand(problem):
            if child.state not in reached or child.path_cost<reached[child.state].path_cost:
                frontier.put((1,child))
                nodeColors[child.state] = "orange"
                steps += 1
                allNodeColors.append(dict(nodeColors))

                reached.update({child.state:child})

        # modify the color of explored nodes to blue
        nodeColors[node.state] = "blue"
        steps += 1
        allNodeColors.append(dict(nodeColors))
            
      return None

    return program