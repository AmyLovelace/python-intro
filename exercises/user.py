
class User:
  
  def __init__(self,name,prof,age,alive=True):
    self.__name = name;
    self.__prof = prof;
    self.__age = age;
    self.alive = alive
    
  def get_name(self):
    return self.__name

  def get_prof(self):
    return self.__prof

  def get_age(self):
    return self.__age

  def hello(self):
    print(f"My name is {self.__name} and I'm {self.get_age()} years old ,you old biatch")
    
