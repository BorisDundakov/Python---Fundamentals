number = (input())

numbers_as_list = list(map(int, str(number)))
reversed_array = (sorted(numbers_as_list, reverse=True))

print(''.join(map(str, reversed_array)))
