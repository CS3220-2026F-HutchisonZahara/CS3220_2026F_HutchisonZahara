from src.thingClass import Thing

class Food(Thing):

    def __init__(self,weight=100,calories=200):
        #weight and calories
        self.weight=weight
        self.calories = calories
        self.energy = self.weight*self.calories

    def sayHi():
        pass
        
class Milk(Food):
    def sayHi(self):
        print("There is a milk")

class Sausage(Food):
    def sayHi(self):
        print("There is a sausage")

class Mouse(Food):
    def __init__(self, size=1):
        self.size=size
        self.weight=None
        self.calories = None
        self.energy=self.size*1000


    def sayHi(self):
        print(f"There is a Mouse with a power {self.energy}")


milk=Milk(weight=200,calories=50)
sausage=Sausage(weight=150,calories=505)
mouse=Mouse(size=2)
