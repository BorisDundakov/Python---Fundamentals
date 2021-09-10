n_snowballs = int(input())
snowball_snow = 0
snowball_time = 0
snowball_quality = 0
snowball_value = 0
value_list = []
snow_list = []
time_list = []
quantity_list = []

for snowballs in range(n_snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = int((snowball_snow / snowball_time) ** snowball_quality)
    value_list.append(snowball_value)
    snow_list.append(snowball_snow)
    time_list.append(snowball_time)
    quantity_list.append(snowball_quality)

    snowball_value = 0

snowball_value = max(value_list)
index = value_list.index(max(value_list))

# the index of the snowball value with the corresponding index position of the time, snow and quantity list
# example: biggest value is at index 2, we need to print the time, snow and quantity at index 2 for the correspond lists

print(f"{snow_list[index]} : {time_list[index]} = {int(snowball_value)} ({quantity_list[index]})")

