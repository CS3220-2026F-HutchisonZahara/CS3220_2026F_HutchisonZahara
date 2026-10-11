import random
from enum import Enum

import numpy as np

LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3

# Actions dictionary
actions_dict = {
    LEFT: 'left',
    UP: 'up',
    RIGHT: 'right',
    DOWN: 'down',
}


class Action(str, Enum):
    LEFT = 'left'
    UP = 'up'
    RIGHT = 'right'
    DOWN = 'down'

    def __str__(self):
        return self.value


left, up, right, down = Action.LEFT.__str__(), Action.UP.__str__(), Action.RIGHT.__str__(), Action.DOWN.__str__()


def makeMaze(n):
    size = (n, n)
    debrisProbability = 0.25
    droneProbability = 0.1
    arrMaze = np.random.choice(
        [0, 1, 2], size=size, p=[1 - debrisProbability - droneProbability, debrisProbability, droneProbability]
    )

    zeroIdx = np.flatnonzero(arrMaze == 0)
    idx = np.random.choice(zeroIdx, size=2, replace=False)
    arrMaze.flat[idx[0]] = 3
    arrMaze.flat[idx[1]] = 4
    return arrMaze


def defineMazeActions(arr):
    n = arr.shape[0]
    maze_actions = {}
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                maze_actions.setdefault((i, j), [right, down])
            elif i == 0 and j == n - 1:
                maze_actions.setdefault((i, j), [left, down])
            elif i == n - 1 and j == 0:
                maze_actions.setdefault((i, j), [up, right])
            elif i == n - 1 and j == n - 1:
                maze_actions.setdefault((i, j), [left, up])
            elif i == 0:
                maze_actions.setdefault((i, j), [left, right, down])
            elif i == n - 1:
                maze_actions.setdefault((i, j), [left, up, right])
            elif j == 0:
                maze_actions.setdefault((i, j), [up, right, down])
            elif j == n - 1:
                maze_actions.setdefault((i, j), [left, up, down])
            else:
                maze_actions.setdefault((i, j), [left, up, right, down])
    return maze_actions


def defineMazeAvailableActions(arr):
    n = arr.shape[0]
    maze_available_actions = {}
    for i in range(n):
        for j in range(n):
            maze_available_actions.setdefault((i, j), [left, up, right, down])
            if arr[i, j] == 1:  # inside wall
                maze_available_actions[i, j] = []
                continue
            if i + 1 >= n or arr[i + 1, j] == 1:
                maze_available_actions[i, j].remove(down)
            if i - 1 < 0 or arr[i - 1, j] == 1:
                maze_available_actions[i, j].remove(up)
            if j + 1 >= n or arr[i, j + 1] == 1:
                maze_available_actions[i, j].remove(right)
            if j - 1 < 0 or arr[i, j - 1] == 1:
                maze_available_actions[i, j].remove(left)
    return maze_available_actions


def makeMazeTransformationModel(mazeActs):
    mazeStateSpace = {}
    for key in mazeActs:
        for action in mazeActs[key]:
            if action == 'left':
                x = key[0]
                y = key[1] - 1
                mazeStateSpace.setdefault(key, {})[action] = (x, y)
            elif action == 'up':
                x = key[0] - 1
                y = key[1]
                mazeStateSpace.setdefault(key, {})[action] = (x, y)
            elif action == 'right':
                x = key[0]
                y = key[1] + 1
                mazeStateSpace.setdefault(key, {})[action] = (x, y)
            elif action == 'down':
                x = key[0] + 1
                y = key[1]
                mazeStateSpace.setdefault(key, {})[action] = (x, y)
        if len(mazeActs[key]) == 0:
            mazeStateSpace.setdefault(key, {})

    return mazeStateSpace


def mazeStatesRandomLocations(n):
    x = []
    y = []
    keyList = []
    for i in range(n):
        for j in range(n):
            keyList.append((i, j))

    # print(keyList)
    for _ in range(len(keyList)):
        x.append(random.randint(0, n + 1))
        y.append(random.randint(0, n + 1))
    zipped = zip(x, y)
    return dict(zip(keyList, zipped))


def mazeStatesLocations(keyList):
    x = []
    y = []

    for elem in keyList:
        x.append(elem[1] * 50)
        y.append(elem[0] * 50)

    zipped = zip(x, y)
    return dict(zip(keyList, zipped))


def intTupleTostr(t):
    return "-".join(str(item) for item in t)
