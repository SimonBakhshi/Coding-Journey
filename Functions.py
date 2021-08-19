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
