from src.agentPrograms import *
from src.agentClass import Agent, MouseAgent, proCatAgent

from src.rules import vacuumRules
from src.rules import actionList
from src.rules import table

#your code here
from src.rules import a2proRules
from src.rules import catRules, cat2Rules, mouseAgentLocations




'''Randomly choose one of the actions from the vacuum environment'''
def RandomVacuumAgent():
    return Agent(RandomAgentProgram(actionList))


def TableDrivenVacuumAgent():
     return Agent(TableDrivenAgentProgram(table))
 
 
def ReflexAgent() :
  return Agent(ReflexAgentProgram(vacuumRules,interpret_input,rule_match))


def ReflexAgentA2pro():
    pass
    #your code here for the Task1
    


def ReflexAgentA3pro():#cat Agent
    pass
    #your code here for the Task2


def RandomMouseAgent():
    return MouseAgent(RandomAgentProgram(mouseAgentLocations))


def ReflexAgentA4pro():#cat Agent for mouse Agent
    return proCatAgent(ReflexAgentProgram(cat2Rules,interpret_input_A4pro,rule_match))
    

