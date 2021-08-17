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

# test 2