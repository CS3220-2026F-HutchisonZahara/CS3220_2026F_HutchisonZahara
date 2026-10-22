# from src.agentPrograms import *
# from src.agentClass import Agent

# from src.rules import vacuumRules
# from src.rules import actionList
# from src.rules import table




# '''Randomly choose one of the actions from the vacuum environment'''
# def RandomVacuumAgent():
#     return Agent(RandomAgentProgram(actionList))


# def TableDrivenVacuumAgent():
#      return Agent(TableDrivenAgentProgram(table))
 
 
# def ReflexAgent() :
#   return Agent(ReflexAgentProgram(vacuumRules,interpret_input,rule_match))


# def ReflexAgentA2pro():
#     pass
#     #your code here
  

# for the Assignment3

import math

from src.PS_agentPrograms import A_StarSearchAgentProgram, IDA_StarSearchAgentProgram, RBFS_SearchAgentProgram, manhat_dist
from src.mazeProblemSolvingAgentSMARTClass import MazeProblemSolvingAgentSMART
#from vacuumProblemSolvingAgentShowClass import VacuumProblemSolvingAgentDraw
#from src.navProblemSolvingAgentClass import navProblemSolvingAgent

def ProblemSolvingMazeAgentAstar(initState,mazeWorldGraph,goalState):
    #Astar_AP_EvcDist=A_StarSearchAgentProgram(math.dist)
    #return MazeProblemSolvingAgentSMART(initState,mazeWorldGraph,goalState,Astar_AP_EvcDist)
    return MazeProblemSolvingAgentSMART(initState,mazeWorldGraph,goalState,A_StarSearchAgentProgram(math.dist))

# task 2
def ProblemSolvingMazeAgentAstarManhat(initState, mazeWorldGraph, goalState):
    return MazeProblemSolvingAgentSMART(initState, mazeWorldGraph, goalState, A_StarSearchAgentProgram(manhat_dist))

# task 7
def ProblemSolvingMazeAgentIDAstar(initState, mazeWorldGraph, goalState):
    return MazeProblemSolvingAgentSMART(initState, mazeWorldGraph, goalState, IDA_StarSearchAgentProgram(manhat_dist))

# task 8
def ProblemSolvingMazeAgentRBFS(initState, mazeWorldGraph, goalState):
    return MazeProblemSolvingAgentSMART(initState, mazeWorldGraph, goalState, RBFS_SearchAgentProgram(manhat_dist))


# def ProblemSolvingMazeAgentBFS(initState,mazeWorldGraph,goalState):
#     return MazeProblemSolvingAgentSMART(initState,mazeWorldGraph,goalState,BestFirstSearchAgentProgram())

 
# def ProblemSolvingNavAgentBFS(initState,WorldGraph,goalState):
#     return navProblemSolvingAgent(initState,WorldGraph,goalState,BestFirstSearchAgentProgram())

# def ProblemSolvingVacuumAgentBFSwithShow(initState,vacuumWorldGraph,goalState):
#     return VacuumProblemSolvingAgentDraw(initState,vacuumWorldGraph,goalState,BestFirstSearchAgentProgramForShow())