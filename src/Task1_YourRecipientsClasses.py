from src.thingClass import Thing

class OfficeManager(Thing):
  
  #pass
  def __init__(self, name="Joe"):
    self.name=name
    print(f"I am OfficeManager {self.name}")
#you code here

class ITStaff(Thing):
  #pass
  def __init__(self, name="Jack"):
    self.name=name
    print(f"I am ITStaff {self.name}")
#you code here

class Student(Thing):
  #pass
  def __init__(self, name="Hanna"):
    self.name=name
    print(f"I am Student {self.name}")
#you code here