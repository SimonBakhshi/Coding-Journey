inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# Counted inventory
len(inventory)
inventory_len = len(inventory)

#Selecting first element in inventory
inventory[0] 
first = inventory[0] 
inventory[-1]
last = inventory[-1]

# Selecting items
inventory[2:6]
inventory_2_6 = inventory[2:6]
inventory[:3]
first_3 = inventory[:3]

# Counting twin beds in inventory
inventory.count("twin bed")
twin_beds = inventory.count("twin bed")


# Removing item from inventory
inventory.pop(-14)
removed_item = inventory.pop(-14)


# Adding item to inventory list
inventory.insert(10, "19th Century Bed Frame")


# Sorting inventory
sorted_list = sorted(inventory)
print(sorted_list)
inventory.sort(reverse=True)
print(inventory)