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