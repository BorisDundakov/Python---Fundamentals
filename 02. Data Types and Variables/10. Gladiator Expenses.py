n_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
day = 0
expenses = 0
broken_shield_counter = 0

for damages in range(n_lost_fights):
    day += 1
    if day % 2 == 0 and day % 3 != 0:
        expenses += helmet_price
    if day % 3 == 0:
        expenses += sword_price
        if day % 2 == 0:
            expenses += helmet_price
            expenses += shield_price
            broken_shield_counter += 1
            if broken_shield_counter % 2 == 0:
                expenses += armor_price

print(f"Gladiator expenses: {expenses :.2f} aureus")