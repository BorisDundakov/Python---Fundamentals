number_of_lines = int(input())
is_Filled = False
water_tank_capacity = 255
capacity_filled = 0
liters_in_tank = 0
total_error_counter = 0

for i in range(number_of_lines):
    liters_of_water = int(input())
    capacity_filled += liters_of_water

    if capacity_filled > water_tank_capacity:
        total_error_counter += 1
        capacity_filled -= liters_of_water
        is_Filled = True

if not is_Filled:
    print(capacity_filled)

else:
    print("Insufficient capacity!\n" * total_error_counter, end="")
    print(capacity_filled)

