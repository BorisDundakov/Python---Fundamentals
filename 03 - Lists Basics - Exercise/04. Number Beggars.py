list_of_numbers_as_String = input().split(", ")
n_beggars = int(input())
sums_of_each_beggar = []
start_index = 0

for beggar in range(n_beggars):
    current_sum = 0
    for sum_index in range(start_index, len(list_of_numbers_as_String), n_beggars):
        current_sum += int(list_of_numbers_as_String[sum_index])
    sums_of_each_beggar.append(current_sum)
    start_index += 1
print(sums_of_each_beggar)
