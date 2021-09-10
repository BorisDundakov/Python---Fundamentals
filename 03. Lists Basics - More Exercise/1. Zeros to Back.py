numbers = input().split(", ")

integer_map = map(int, numbers)
integer_numbers = list(integer_map)
final_list = []
zeroes_list = []

for i in range(len(integer_numbers)):
    if (integer_numbers[i]) == 0:
        zeroes_list.append(integer_numbers[i])
    else:
        final_list.append(integer_numbers[i])

for j in range(len(zeroes_list)):
    final_list.append(zeroes_list[j])

print(final_list)