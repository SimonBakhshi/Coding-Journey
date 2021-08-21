# Creating a function which tells the user they can use the public subway to visit central park in New York:
def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)

generate_trip_instructions("Central Park")

# Creating a function which calculates the total expenses of a users trip. Plane ticket, car rental, hotal rate and trip time - discount.:
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  print("Your total expenses: ") 
  print(car_rental_total + hotel_total + plane_ticket_price)

# Creating trip planner: 
def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ",then " + second_destination + " and lastly " + final_destination)

trip_planner("Brooklyn", "Queens")

# Creating a function which deducts the expenses of the users starting budget:
current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

shirt_expense = 9
def deduct_expense(budget, expense):
  return budget - expense 
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)
print_remaining_budget(new_budget_after_shirt)

# Creating af function which returns the top travel destinations in Italy:
def top_tourist_locations_italy():
  first = "Rome" 
  second = "Venice"
  third = "Florence"
  return first, second, third

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()
print(most_popular1)
print(most_popular2)
print(most_popular3)

# Creating TripPlanner v1.0
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

# Running program
trip_planner_welcome("Simon ")
estimate = estimated_time_rounded(10.77)
destination_setup(" Silkeborg ", "København ", estimate, "Car")

# Variables 
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Creating Fahrenheit to celsius and celsius to fahrenheit converteres: 
def f_to_c(f_temp):
  c_temp = (f_temp -32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp = c_temp *(9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# Creating a function which multiplies mass and acceleration:
def get_force(mass, acceleration):
  mass_times_acceleration = mass * acceleration
  return mass_times_acceleration

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies ", train_force, " Newtons of force")

# Creating a function which calculates the energy contained in a bomb in joules of energy:
def get_energy(mass, c=3*10**8):
  mass_times_c2 = mass * c**2
  return mass_times_c2

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies", bomb_energy, "Joules.")

# Creating a function which calculates the amount of work the GE train does in 100 meters. The work is calculated in joules of energy.  
def get_work(mass, acceleration, distance):
  force_multiplied_by_distance = get_force(mass, acceleration) * distance
  return force_multiplied_by_distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does", train_work, "Joules of work over", train_distance, "meters.")

# Function calculating base to the power of exponent. The program returns boolean values whether the number is greater or lesser than 5000.
def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else: 
    return False
    
print(large_power(2, 13))
print(large_power(2, 12))

# Writing a program which calculates whether the spendings of a customer surpasses their budget.
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if food_bill + electricity_bill + internet_bill + rent > budget:
    return True
  else:
    return False

print(over_budget(100, 20, 30, 10, 40))
print(over_budget(80, 20, 30, 10, 30))

# Writing a program which calculates whether a number is twice as large as another:
def twice_as_large(num1, num2):
  if num1 > num2 * 2:
    return True
  else:
    return False

print(twice_as_large(10, 5))
print(twice_as_large(11, 5))

# Writing a function which checks whether the input number is divisible by ten:
def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  else:
    return False

print(divisible_by_ten(20))
print(divisible_by_ten(25))

# Creating a program which checks whether two numbers added together equals ten or not. Returns the calculation i booleans. 
def not_sum_to_ten(num1, num2):
  if num1 + num2 != 10:
    return True
  else:
    return False

print(not_sum_to_ten(9,-1))
print(not_sum_to_ten(9, 1))
print(not_sum_to_ten(5,5))

# Writing a program which checks whether num is greater than or equal to lower and if num is less than or equal to upper: 
def in_range(num, lower, upper):
  if num >= lower and num <= upper:
    return True
  return False

print(in_range(10, 10, 10))
print(in_range(5, 10, 20))

# Writing a function which compares if your_name and my_name are ==. It returns the input in Boolean values: 
def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  else:
    return False

# Creating a contradictory function: In the example the input number cannot both be greater than and less than 0, that is a contradiction:  
def always_false(num):
  if num > 0 and num < 0:
    return True
  return False

print(always_false(0))
print(always_false(-1))
print(always_false(1))

# Creating a function which depending on a movies rating reccomends it to them or tells people to avoid it:
def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif rating < 9:
    return "This one was fun."
  else:
    return "Outstanding!"
    
print(movie_review(9))
print(movie_review(4))
print(movie_review(6))

# Writing a function which compares the 3 numbers in the function def max_num(num1, num2, num3): and returns which number is the greater number. If there is a tie it returns "It's a tie!":
def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!" 

print(max_num(-10, 0, 10))
print(max_num(-10, 5, -30))
print(max_num(-5, -10, -10))
print(max_num(2, 3, 3))

# This function appends the index length of the list to itself. List + x index in list:
def append_size(lst):
  lst.append(len(lst))
  return lst

print(append_size([23, 42 ,67]))





