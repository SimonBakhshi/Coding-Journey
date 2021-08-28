# Merging lists:
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_B:
  students_period_A.append(student)
print("This is the merged list:")
print(students_period_A)


# Creting for loop break when dalmatian is found:
dog_breeds_available_for_adoption = ["french bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)    
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!") 
    break


# Creating a continue loop. It returns the ages over 21:
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for less in ages:
  if less < 21:
    continue
  print(less)


# Looping through sales data:
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data:
  print(location)
  # Calculating the sum of sales_data:
  for number in location:
    scoops_sold += number
print(scoops_sold)

# Scaling grades:
grades = [90, 88, 62, 76, 74, 89, 48, 57]

scaled_grades = [num + 10 for num in grades]
print(scaled_grades)

#Creating a for loop that calls all heights above 161:
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)

# Lists:
single_digits = range(0, 10)
squares = []

# Digits squared:
for digits in single_digits: 
  print(digits)
  squares.append(digits ** 2)
print(squares)

# Digits in 3th:
cubes = [cubes ** 3 for cubes in single_digits]
print(cubes) 

# Program that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam and prints Greetings if anything else is stored in spam:
spam = ""
if 1 == spam:
  print("Hello")
elif 2 == spam:
  print("Howdy")
else:
  print("Greetings")

# A for loop printing numbers 0-9:
for i in range(10):
  print(i)
  
# A while loop printing number 0-9:
count = 0
while count < 10:
  print(count)
  count += 1
  
# Creating a list which stores user input using a while loop:
# friend_names = []
# while True:
#   print("Please enter the name of friend " + str(len(friend_names) + 1 ) + " (Or enter nothing to stop.):")
#   name = input()
#   if name == "":
#     break
#   friend_names = friend_names + [name] # list concatenation
# print("Friend names are:")
# for name in friend_names:
#   print("" + name)

# This program lets a customer enter a computer game. If the computer game is on the list the program lets the customer know where they can buy the game. If the game is not on the list the program informs the customer the game is not available:   
computer_games = [["Fifa", "25$"], ["Call of duty", "60$"], ["Fortnite", "10$"], ["Resident Evil", "15$"], ["Tony Hawks pro skater", "60$"], ["GTA 5", "20$"], ["Batman Arkham Knight", "5$"], ["Control", "30$"]]
print("Welcome to Simon's Super Shelf. Enter a computer game and we will check if the game is in store:")
name = input()
for r in computer_games:
  for c in r:
#for i in range(len(computer_games)):
    if name not in c:
     print("Sorry but we do not have the game you entered") 
    else:
      print(name + " is on the shelf in our shop downtown. You can also buy the game in our online store.")
      
  
    
    
    
    
    
    # print("Do you want to now the price of the game?")
#   input()
#   if "yes":
#     print("price")
#   else:
#     print("Maybe you are more interested in some other games?")