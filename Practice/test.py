import math


from pprint import pprint as pp

ls = [["Name", "Base_Cost", "Add-Ons", "Tax", "Drink_cost", "Charity", "Tip", "Final_Cost"]]


def find_base_cost(size):
    if size == "s":
        return 5.00
    elif size == "m":
        return 6.25
    else:
        return 7.00


def find_add_ons(cream, sugar):
    cream_cost = 0
    sugar_cost = 0
    if cream == "y":
        cream_cost = 0.75
    if sugar == "y":
        sugar_cost = 0.2
    return cream_cost + sugar_cost


def calculate_tax(base_cost, add_ons):
    return (base_cost + add_ons) * 0.0875

def calculate_charity(charity, drink_cost):
    if charity == "n":
        return 0
    else:
        return math.ceil(drink_cost) - drink_cost


text = open("CoffeeOrders.py", "r")
no_of_orders = 0
while True:
    ls1 = []
    # Name
    name = text.readline().strip("\n")
    if name == "END":
        break
    no_of_orders += 1
    ls1.append(name)


    # Base cost
    size = text.readline().lower().strip("\n")
    base_cost = find_base_cost(size)
    ls1.append(base_cost)

    # Add-ons
    cream = text.readline().lower().strip("\n")
    sugar = text.readline().lower().strip("\n")
    add_ons = find_add_ons(cream, sugar)
    ls1.append(add_ons)

    # Tax
    tax = calculate_tax(base_cost, add_ons)
    ls1.append(tax)

    # Drink_cost
    drink_cost = base_cost + add_ons + tax
    ls1.append(drink_cost)

    # Charity
    charity = text.readline().lower().strip("\n")
    charity_amt = calculate_charity(charity, drink_cost)
    ls1.append(charity_amt)

    # Tip
    tip = float(text.readline().strip("\n"))
    ls1.append(tip)

    # Final cost
    final_cost = drink_cost + charity_amt + tip
    ls1.append(final_cost)
    ls.append(ls1)

# Printing the table
# Headers
for i in range(len(ls[0])):
    if i == 0:
        print(f"{ls[0][i]:<10}", end="")
    else:
        print(f"{ls[0][i]:>15}", end="")
print()
print("-"*115)
# Rows
for i in range(1, len(ls)):
    for j in range(len(ls[0])):
        if j == 0:
            print(f"{ls[i][j]:<10}", end="")
        else:
            print(f"{ls[i][j]:>15.2f}", end="")
    print()
print("-"*115)

# Summary
total_charity = 0
for i in range(1, no_of_orders + 1):
    total_charity += ls[i][5]

total_tips = 0
for i in range(1, no_of_orders + 1):
    total_tips += ls[i][6]

money_spent = 0
for i in range(1, no_of_orders + 1):
    money_spent += ls[i][7]

print("Totals:")
print(f"\tNumber of oredrs:  {no_of_orders}")
print("\t{:<17}" .format("Charity donation:"), end=" ")
print("$", end="")
print(f"{total_charity:>7.2f}")

print("\t{:<17}" .format("Total tips:"), end=" ")
print("$", end="")
print(f"{total_tips:>7.2f}")

print("\t{:<17}" .format("Money spent:"), end=" ")
print("$", end="")
print(f"{money_spent:>7.2f}")
print()
text.close()
