class Circle:
  pi = 3.14
  def area(self, radius):
    area = self.pi * radius ** 2
    return area
  
circle = Circle()
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)
print(pizza_area, teaching_table_area, round_room_area)

# Constructor method __init__:
class Circle:
  pi = 3.14
  
  # Constructor:
  def __init__(self, diameter):
    print("New circle with diameter: {diameter}".format(diameter=diameter))
  

teaching_table = Circle(36) 

# Initiation of two different objects from a class:
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()
alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

# This Class initiates instances of circles:
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    
    self.radius = diameter / 2
  
  def circumference(self):
    return 2 * self.pi * self.radius
    
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

# String representation using dunder method __repr__:
class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)
  
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)

# The first class creates a tablet in the method def __init__ for students to be instantiated objects. 
# furthermore it creates a method called add_grade which checks if the type grade is equal to the Class grade. 
# If it's the case it appends the grade to a list grades. 
class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
    
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)
    
  def get_average(self):
    value = 0
    for grade in self.grades:
      value += grade
    return value / len(self.grades)

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))
print(Student.get_average())

# Inheritance and raise exception:
class OutOfStock(Exception):
  pass 

class CandleShop:
  name = "Here's a Hot Tip: Buy Drip Candles"
  def __init__(self, stock):
    self.stock = stock
    
  def buy(self, color):
    if self.stock[color] < 1:
      raise OutOfStock
    self.stock[color] = self.stock[color] - 1

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')


candle_shop.buy('green')

# Admin inheritance rights
class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text

class User:
  def __init__(self, username):
    self.username = username
    
  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text

class Admin(User):
  def edit_message(self, message, new_text):
      message.text = new_text