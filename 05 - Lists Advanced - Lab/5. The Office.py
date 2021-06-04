numbers_as_int = [int(el) for el in input().split()]
h_factor = int(input())
list_average = 0
greater_than_average = []
are_Happy = False

for el in range(len(numbers_as_int)):
    numbers_as_int[el] *= h_factor
    list_average += numbers_as_int[el]

list_average /= len(numbers_as_int)

for element in range(len(numbers_as_int)):
    if numbers_as_int[element] >= list_average:
        greater_than_average.append(numbers_as_int[element])


if len(greater_than_average) >= len(numbers_as_int) / 2:
    are_Happy = True


if are_Happy:
    print(f"Score: {len(greater_than_average)}/6. Employees are happy!")
else:
    print(f"Score: {len(greater_than_average)}/6. Employees are not happy!")