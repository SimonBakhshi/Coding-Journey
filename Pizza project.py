# Pizza project:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

# Counting:
prices.count(2)
num_two_dollar_slices = prices.count(2)

# toppings list length:
len(toppings)
num_pizzas = len(toppings)

# Adding string: Husk hvordan begge strings og funktionen num_pizzas + sammen. num_pizzas converteres til en string og skrives/printes ud sammen med begge strings.
print("We sell " + str(num_pizzas) + " different kinds of pizza!") 

# Converting toppings and prices:
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

# Sorting pizzas according to ascending prices:
pizza_and_prices.sort()

# Sorting cheapest pizza:
cheapest_pizza = pizza_and_prices

# Calling priciest pizza from list:
priciest_pizza = pizza_and_prices[-1]

# Removeing anchovies from list:
pizza_and_prices.pop()

# Adding topping to list:
pizza_and_prices.insert(4, [2.5, "peppers"])

# Slicing pizza_and_prices list --> cheapest to new list:
three_cheapest = pizza_and_prices[:3]
