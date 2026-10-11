from src.mazeData import LEFT, UP, RIGHT, DOWN

moves = {LEFT: (0, -1), UP: (-1, 0), RIGHT: (0, 1), DOWN: (1, 0)}


def defineLabAvailableActions(maze):
  n = maze.shape[0]
  labActions = {}
  for i in range(n):
    for j in range(n):
      if maze[i, j] == 1:
        continue
      labActions[(i, j)] = []
      for action, (di, dj) in moves.items():
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n and maze[ni, nj] != 1:
          labActions[(i, j)].append(action)
  return labActions


def isLabNode(cell, labActions, start, goal):
  return cell == start or cell == goal or len(labActions[cell]) != 2


def nextCell(cell, action):
  di, dj = moves[action]
  return (cell[0] + di, cell[1] + dj)


def walkCorridor(cell, action, labActions, start, goal):
  path = [nextCell(cell, action)]
  while not isLabNode(path[-1], labActions, start, goal):
    back = (action + 2) % 4
    action = [a for a in labActions[path[-1]] if a != back][0]
    path.append(nextCell(path[-1], action))
  return path


def makeLabTransformationModel(labActions, start, goal):
  labTM = {}
  labPaths = {}
  for cell in labActions:
    if not isLabNode(cell, labActions, start, goal):
      continue
    labTM[cell] = {}
    for action in labActions[cell]:
      path = walkCorridor(cell, action, labActions, start, goal)
      labTM[cell][action] = path[-1]
      labPaths[(cell, action)] = path
  return labTM, labPaths
