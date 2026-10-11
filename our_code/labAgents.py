from src.PS_agentPrograms import BestFirstSearchAgentProgram
from our_code.rescueRobotClass import RescueRobotAgent
from our_code.labAgentPrograms import UniformCostSearchAgentProgram, IDSearchAgentProgram


def RescueRobotBFS(initState, labGraph, goalState, labPaths):
  return RescueRobotAgent(initState, labGraph, goalState, labPaths, BestFirstSearchAgentProgram(), "BFS-Robot")


def RescueRobotUCS(initState, labGraph, goalState, labPaths):
  return RescueRobotAgent(initState, labGraph, goalState, labPaths, UniformCostSearchAgentProgram(), "UCS-Robot")


def RescueRobotIDS(initState, labGraph, goalState, labPaths):
  return RescueRobotAgent(initState, labGraph, goalState, labPaths, IDSearchAgentProgram(), "IDS-Robot")
