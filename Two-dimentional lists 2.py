# Your code below: 
first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"] 
preferred_size.append("Medium")
print(preferred_size)

# Helping Maria visualize:
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)
customer_data[1].remove("Large")
print(customer_data)

# Editing Chanis order:
customer_data[2][2] = False
print(customer_data)