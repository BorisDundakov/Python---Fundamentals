allowed_quantity = int(input())
days_left = int(input())

total_cost = 0
total_Spirit = 0

for current_day in range(1, days_left + 1):
    if current_day % 2 == 0:
        total_cost += 2 * allowed_quantity
        total_Spirit += 5

    if current_day % 3 == 0:
        total_cost += 5 * allowed_quantity
        total_cost += 3 * allowed_quantity
        total_Spirit += 13

    if current_day % 5 == 0:
        total_cost += 15 * allowed_quantity
        total_Spirit += 17

        if current_day % 3 == 0:
            total_Spirit += 30

    if current_day % 10 == 0:
        total_Spirit -= 20
        total_cost += 5 + 3 + 15

        if current_day == days_left + 1:
            total_Spirit -= 30

    if current_day % 11 == 0:
        allowed_quantity += 2

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_Spirit}")