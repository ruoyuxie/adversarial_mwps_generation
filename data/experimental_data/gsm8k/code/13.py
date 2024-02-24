# Define the variables based on the problem statement
amandas_gift_money = 50  # Amanda received $50 as a gift
cassette_tape_price = 9   # Price of each cassette tape
headphone_set_price = 25  # Price of the headphone set
number_of_cassette_tapes = 2  # Amanda plans to buy two cassette tapes

# Calculate the total cost of the cassette tapes
total_cassette_tape_cost = cassette_tape_price * number_of_cassette_tapes

# Calculate the total cost of the headphone set
total_headphone_set_cost = headphone_set_price

# Calculate the total cost of all items Amanda plans to buy
total_cost = total_cassette_tape_cost + total_headphone_set_cost

# Calculate how much money Amanda will have left after her purchases
money_left = amandas_gift_money - total_cost

# Print the final answer
print("Amanda will have $" + str(money_left) + " left after her purchases.")