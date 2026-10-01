from src.thingClass import Thing

class Food(Thing):
    def __init__(self, weight=0, calories=0):
        self.weight = weight
        self.calories = calories
        self.energy = round(weight * calories / 1000)

    def sayHi(self):
        print(f"Hi, I am {type(self).__name__} (weight: {self.weight}, calories: {self.calories}, energy: {self.energy})")


class Milk(Food):
    pass

class Sausage(Food):
    pass

class Mouse(Food):
    def __init__(self, size=1):
        super().__init__()
        self.size = size
        self.energy = size * 1000

    def sayHi(self):
        print(f"Hi, I am Mouse (size: {self.size}, energy: {self.energy})")
