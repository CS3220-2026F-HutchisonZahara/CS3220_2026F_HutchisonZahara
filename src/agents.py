from src.agentPrograms import *
from src.agentClass import Agent

from src.rules import vacuumRules
from src.rules import actionList
from src.rules import table

#your code here
from src.rules import a2proRules
from src.rules import catRules




'''Randomly choose one of the actions from the vacuum environment'''
def RandomVacuumAgent():
    return Agent(RandomAgentProgram(actionList))


def TableDrivenVacuumAgent():
     return Agent(TableDrivenAgentProgram(table))
 
 
def ReflexAgent() :
  return Agent(ReflexAgentProgram(vacuumRules,interpret_input,rule_match))


def ReflexAgentA2pro():
    #pass
    #your code here
    return Agent(ReflexAgentProgram(a2proRules,interpret_input_A2pro,rule_match_A2pro))


def ReflexAgentA3pro():#cat Agent
    #pass
    #your code here
    return Agent(ReflexAgentProgram(catRules,interpret_input_A3pro,rule_match_A2pro))

