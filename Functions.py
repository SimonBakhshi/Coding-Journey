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

# Creating TripPlanner v1.0:
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

# Creating Fahrenheit to celsius and celsius to fahrenheit converteres: 
def f_to_c(f_temp):
  c_temp = (f_temp -32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(37)
print(c0_in_fahrenheit)

# Creating a function which multiplies mass and acceleration:
# Variables 
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

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

# Creating a function which depending on a movies rating recommends it to people or tells them to avoid it:
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

# Writing a function which compares the 3 numbers in the function def max_num(num1, num2, num3): and returns which number is the greater number. 
# If there is a tie it returns "It's a tie!":
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

# This function adds the last two index values of lst together and appends the value to itself. 
# It repeats the operation 2 more times and appends the calculated value of lst[-1] + lst[-2] to itself:
def append_sum (lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst
  
print(append_sum([1, 1, 2]))

# This function returns the last index [-1] of the list which contains more elements. 
# If both lists are equal in size it retuns the last index value of lst1:
def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# This function counts the number of times the parameter item e.g. (Werthers orginal candy) appears on lst. 
# It compares whether the count is greater than the value n e.g. (n = 3) and returns the answer in Boolean values:    
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

# This function combines two lists and sorts them. It then returns the sorted list:
def combine_sort(lst1, lst2):
  unsorted = lst1 + lst2
  sorted_list = sorted(unsorted)
  return sorted_list

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

# This function returns a list from the parameter number to 100 by increments of 3. If the parameter number is > than 100 it returns an empty list:
def every_three_nums(start):
 return list(range(start, 101, 3))
 
print(every_three_nums(91))

# This functions slices the indexes between the parameters start and end including the end index number itself: 
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]
  
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# This function counts the parameters item1 and item2 and compares which of the parameters appears on the list most times. 
# It returns the parameter which shows up most times. If the parameters appear the same number of times the function returns the parameter item1: 
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2
    
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# This function checks if the index value is invalid compared with lst's length. If thats the case it returns lst. 
# Otherwise it returns a new list called lst2 where the index parameter in the function is multiplied by 2: 
def double_index(lst, index):
  if index >= len(lst):
    return lst
  else:
    lst2 = lst[0:index]
    lst2.append(lst[index]*2)
    lst2 = lst2 + lst[index+1:]
    return lst2
    
print(double_index([3, 8, -10, 12], 2))

# This function finds the middle item from a list of values. This differs depending on whether there are an odd or even number of values on the list. 
# If the list contain an odd number of elements the function returns the exact middle value of the list. 
# If the list is even it returns the average of the middle two elements of the list:   
def middle_element(lst):
  if len(lst) % 2 == 0:
     sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) -1]
     return sum / 2
  else: 
    return lst[int(len(lst)/2)]

print(middle_element([5, 2, -10, -4, 4, 5,]))

# This function loops through the parameter nums and checks whether the numbers in nums are divisible with 10. 
# For every number divisible by 10 the counter is incremented. The function returns the count of how many numbers in nums are divisible by 10:
def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count +=1
  return count

print(divisible_by_ten([20, 25, 30, 35, 40]))

# This function concatenate "Hello, " with each name in the parameter names and appends the new string to the string names_and_greetings.  
def add_greetings(names):
  names_and_greetings = []
  for name in names:
    names_and_greetings.append("Hello, " + name)
  return names_and_greetings
   
print(add_greetings(["Owen", "Max", "Sophie", "Joe"]))

# This function uses a for loop to iterate through a list checking whether the number at the given index is even or odd. 
# The for loop continues to iterate through the list until it encounter a odd number. 
# The function then returns the list from the odd number till its end, including the index of the odd number itself.
def delete_starting_evens(lst):
  for i, n in enumerate(lst):
    if n % 2 == 0:
      continue
    else:
      return lst[i:]
  return []

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# This function uses a for loop to iterate through a list. 
# If the index number in the list is odd it appends the element/value at the odd index number to a new list named lst2, and returns lst2:
def odd_indices(lst):
  lst2 = []
  for i, e in enumerate(range(len(lst))):
    if i % 2 == 1:
      lst2.append(lst[e])
  return lst2
  
print(odd_indices([4, 3, 7, 10, 11, -2]))

# This function uses two nested for loops to iterate through the bases list of numbers and powers list of numbers. 
# It then returns the result of every number in bases raised to every number in powers in a list called result:  
def exponents(bases, powers):
  result = []
  for b in bases:
    for p in powers:
     result.append(b ** p)
  return result 

print(exponents([2, 3, 4], [1, 2, 3]))

# This function uses a for loop to sum the numbers in both lst1 and lst2. 
# It compares the total sum of both lists with eachother and returns the list with the greater total sum. 
# If the total sum of both lists are equal the function returns lst1: 
def larger_sum(lst1, lst2):
  lst1_sum = 0
  lst2_sum = 0
  for n in lst1:
    lst1_sum += n
  for n in lst2:
    lst2_sum += n
  if lst1_sum >= lst2_sum:
    return lst1 
  else:
    return lst2

 # Another solution to the same problem above:
 def larger_sum(lst1, lst2):
  if sum(lst1) >= sum(lst2):
    return lst1
  return lst2
    
print(larger_sum([1, 9, 5], [2, 3, 7]))

# This function uses a for loop to sum the numbers in a list. 
# A break statement is applied to exit the loop when the count of the numbers in lst reaches or exceeds 9000. 
# This will continue to execute the code outside of the loop, which in this case, returns the sum that reached or exceeded 9000. 
# If the list argument is an empty list the function returns 0:
def over_nine_thousand(lst):
  lst_sum = 0
  for n in lst:
    lst_sum += n
    if lst_sum >= 9000:
      break
  return lst_sum

print(over_nine_thousand([8000, 900, 120, 5000]))

# This function uses a for loop to iterate through a list of numbers. 
# It checks whether the numbers encountered are greater than another list only containing one number. 
# If a number in nums are greater than the number in greatest_num, the function breaks out of the loop and returns the new greatest number:   
def max_num(nums):
  greatest_num = nums[0]
  for n in nums:
    if n > greatest_num:
      break
  return n

# Another solution to the same problem. This function keeps replacing the greatest number encountered with an ealier encountered greatest number. 
# The function above breaks out of the loop when it through its iterations meets a number which is greater than the starting greatest_number. 
# This function on the other hand, keeps iterating through all the numbers in the list. 
# It replaces the greatest number every time it meets a number which is greater than the previous greatest number. 
# Hence it iterates though all the numbers in the list. 
# Whereas the other function breaks out as soon as it encounters the first number greater than the default greatest number:
def max_num(nums):
  greatest_num = nums[0]
  for n in nums:
    if n > greatest_num:
      greatest_num = n
  return greatest_num

print(max_num([50, -10, 0, 75, 20]))

# This function checks whether the values at the same indices in lst1 and lst2 are equal. 
# If so it appends the indices to a list variable called matching_indices and returns the list:  
def same_values(lst1, lst2):
  matching_indices = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]: 
     matching_indices.append(i)
  return matching_indices
  
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# This function checks wheter the second list is the reverse of the first list. It uses a loop to compare if the index value of the inverse list are equal or not.  
# Now in order to get the inverse of the position we are at in the first list, we subtract the index we are at from the end of the second list. 
# So on the first pass, we’ll compare the element at position 0 to the element at position 5 - 1 - 0 = 4. 
# On the next pass, we’ll compare the element at position 1 to the element at position 5 - 1 - 1 = 3, and so on.
# If any of the index values are not equal then the second list aren't the reverse of the first and the function returns False. 
# But if the function made it through the loop without a mismatch the lists are equal and the function retuns True:   
def reversed_list(lst1, lst2):
  for i in range(len(lst1)):
    if lst1[i] != lst2[len(lst2) - 1 - i]:
      return False
  return True

# Solution 2 uses slicing to compare if lst2 is the reverse of lst1:
def reversed_list(lst1, lst2):
    if lst1 == lst2[::-1]:
      return True
    else:
      return False

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1])) 

# This function takes a number as a input value. 
# It uses the try and exception handling to deal with possible problems with the program, if the users input isn't compatible with the function. 
# Regardless whether the user enters a even or odd number, the function returns a sequence of numbers until it reaches the number one. 
# Sooner or later the sequence will arrive at the number 1. This is due to the math used in the function. Even mathematicians aren't sure why it is the case:  
import sys

def collatz(number):
  if number % 2 == 0:
    print(number // 2)
    return number // 2
  
  elif number % 2 == 1:
    result = 3 * number + 1
    print(result)
    return result
try:  
  n = input("Enter a number: ")
  while n != 1:
    n = collatz(int(n))
except KeyboardInterrupt:
  sys.exit()
except ValueError:
  print("The program only accepts a positive integer my friend.")