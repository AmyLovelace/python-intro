def noZero(num):
  while num < 5:
    
    if num %2==0    :
      pass
      
    else:
      print(num)
    num=num + 1  

noZero(0)

from user import User

ami = User("Ami", "Software Engineer", 28)
adel = User("Adel", "Software Engineer", 666)

ami.hello()
adel.hello()

#una funcion que me retorne la long de una string

nombre = "Ami"
apellido="Cabrera"

def lengh_string(name):
  nombre = "andrew tate"
  print(nombre)
  return len(name)

  
print(nombre)

result=lengh_string(nombre)
print(result)

result1=lengh_string(apellido)
print(result1)

#calcula el area de un circulo y que reciba como argumento el radio 
#The area of a circle can be calculated using the formula A = πr², where A is the area of the circle, r is the radius of the circle, and π (pi) is a mathematical constant approximately equal to 3.14159.


class Circle:
  
  def __init__(self, radio):
    self.radio = radio
    self.__pi= 3.14
    
  
  def get_area(self):
    area =self.__pi *(self.radio ** self.radio)
    return area 
  
  
  def get_perimeter(self):
    peri =(2*self.__pi) * self.radio
    return peri
  def rickandmorty(self):
    print("wabadubadudub")
  
  
circle1 = Circle(5)
circle2 = Circle(10)

print(circle1.get_area())
print(circle1.get_perimeter())
print(circle2.get_area())
print(circle2.get_perimeter())
circle2.rickandmorty()
  
age = 17

def underorover(edad):
  
  if edad >= 18:
    print("now you can fuck yourself")
  
  else:
    print("not fuckable yet")



underorover(age)

#funcion que reciba una string y haga print cuando este capitalizado y lowercase

mystring="copito"


def lower_and_upper(string):
  
  print(string.lower())
  print(string.upper())

lower_and_upper(mystring)
  