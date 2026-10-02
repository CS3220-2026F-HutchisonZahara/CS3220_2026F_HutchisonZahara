import random

from src.agentClass import Agent, proCatAgent, MouseAgent
from src.catFriendlyHouse_membersClass import Food, Milk, Sausage, Mouse
from src.environmentProClass import environmentPro
from src.locations import *
from src.thingClass import Thing


# catFriendlyHouse_envClass
class catFriendlyHouse_env(environmentPro):
    def __init__(self):
        super().__init__()
        self.locations = [loc_A, loc_B, loc_C, loc_D]

    def default_location(self, thing):
        print("The item is starting in random location...")
        return random.choice(self.locations)

    def room_state(self, location):
        items = [type(t).__name__ for t in self.list_things_at(location, thingClass=Food)]
        if len(items) == 0:
            return 'Empty'
        if len(items) == 1:
            return items[0]
        return items

    def percept(self, agent):
        self.status = {loc: self.room_state(loc) for loc in self.locations}
        return agent.location, self.status[agent.location]

    def execute_action(self, agent, action):
        # changes the state of the environment based on what the agent does.
        if not self.is_agent_alive(agent):
            return

        if action == 'Drink':
            milk = self.list_things_at(agent.location, thingClass=Milk)[0]
            if agent.drink(milk):
                print(f"The Cat drank {milk} at location: {agent.location}")
                self.delete_thing(milk)

        elif action == 'Eat':
            sausage = self.list_things_at(agent.location, thingClass=Sausage)[0]
            if agent.eat(sausage):
                print(f"The Cat ate {sausage} at location: {agent.location}")
                self.delete_thing(sausage)

        elif action == 'Catch':
            mouse = self.list_things_at(agent.location, thingClass=Mouse)[0]
            if agent.catch(mouse):
                print(f"The Cat caught {mouse} at location: {agent.location}")
            else:
                print(f"The Cat is too weak (performance: {agent.performance}) - the Mouse survived and ran away!")
            self.delete_thing(mouse)

        elif action == 'GoAhead':
            i = self.locations.index(agent.location)
            if agent.direction and i == len(self.locations) - 1:
                agent.changeDirection()
                print("Last room! Some items are still there -> the Cat turns around (Right to Left)")
            elif not agent.direction and i == 0:
                print("The Cat is back in the first room. The hunt is over!")
                agent.alive = False
                return
            agent.location = self.locations[i + 1 if agent.direction else i - 1]
            agent.performance -= 1
            print(f"The Cat moved to location: {agent.location}")

    def is_done(self):
        no_agents = not any(agent.is_alive() for agent in self.agents)
        no_food = len(self.list_things_at_all(Food)) == 0
        return no_agents or no_food

    def list_things_at_all(self, thingClass):
        return [t for t in self.things if isinstance(t, thingClass)]

    # catFriendlyHouse_envClass


class catFriendlyHouse2_env(environmentPro):
    def __init__(self):
        super().__init__()
        self.locations = [loc_A, loc_B, loc_C, loc_D]

    def default_location(self, thing):
        print("The item is starting in random location...")
        return random.choice(self.locations)

    # Return all agants exactly at a given location
    def list_agents_at(self, location, thingClass=Thing):
        return [a for a in self.agents if isinstance(a, thingClass) and a.location == location]

    def percept(self, agent):
        return agent.location, self.list_things_at(agent.location), self.list_agents_at(agent.location)

    def add_thing(self, thing, location=None):  # improved
        # perf = original one not 0 like in parent class
        # from src.agentClass import Agent
        if thing in self.agents:
            print("Can't add the same agent twice")
        else:
            if isinstance(thing, Agent):
                # thing.performance = 0
                thing.location = location if location is not None else self.default_location(thing)
                self.agents.append(thing)
                print(f"Welcome! You are added in location {thing.location}")
        if thing in self.things and thing.location == location:
            print("Can't add the same agent twice")
        else:
            if not isinstance(thing, Agent):
                thing.location = location if location is not None else self.default_location(thing)
                self.things.append(thing)

    def execute_action(self, agent, action):
        # changes the state of the environment based on what the agent does.
        if self.is_agent_alive(agent):
            # the current agent is Cat & Mouse is still there
            if isinstance(agent, proCatAgent) and len(self.agents + self.things) > 0:
                print("Some items are still there ....")

                if action == 'Go ahead' or action == 'Check direction':
                    i = self.locations.index(agent.location)
                    if (agent.direction and i == len(self.locations) - 1) or (not agent.direction and i == 0):
                        agent.changeDirection()
                        print("Last room! Some items are still there -> the Cat turns around")
                    agent.location = self.locations[i + 1 if agent.direction else i - 1]
                    agent.performance -= 5
                    print(f"The Cat moved to location: {agent.location}")

                elif action == 'Catch':
                    mice = [mouse for mouse in self.list_agents_at(agent.location, MouseAgent)]
                    if mice:
                        mouse = mice[0]
                        if agent.performance < mouse.performance * 5:
                            agent.performance -= 10
                            print(
                                f"The Cat is too weak (performance: {agent.performance}) - the Mouse survived and ran away!")
                        else:
                            agent.performance += 10
                            print(f"The Agent did Catch {mouse} at location: {agent.location}")
                            print("There is nothing for Agent Cat here. Done!")
                            self.agents.remove(mouse)
                            agent.alive = False
                    else:
                        print(f"Agent tried to Catch, but no MouseAgent was found at {agent.location}.")

                if agent.performance <= 0:
                    print("The Cat is too weak - Game over")
                    agent.alive = False

            elif isinstance(agent, MouseAgent):
                print(f"the Agent Mouse is still running with a performance {agent.performance}")
                print(f"The Agent Mouse decided to move to {action}")
                agent.location = action
                agent.performance -= 1
                if agent.performance <= 0:
                    agent.alive = False
                    print(f"Agent {agent} is dead.")

    def is_done(self):
        no_agents = not any(agent.is_alive() and isinstance(agent, proCatAgent) for agent in self.agents)
        # return no_agents or no_items
        return no_agents
