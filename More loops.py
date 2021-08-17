hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

# Adding prices to total_price:
for price in prices:
  total_price += price
print(total_price)

average_price = total_price / len(prices)
print("Average Haircut Price: ", average_price)

new_prices = [price -5 for price in prices]
print(new_prices)

# Total revenue:
total_revenue = 0

for i in range(len(hairstyles)):
 total_revenue += prices[i] + last_week[i]
print("Total Revenue: ", total_revenue)

# Dividing total revenue:
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# Advertising haircuts under 30$. Taking the new prices of hairstyles chechking if the cost less than 30$ and printing out the names of the hairstyles:
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)