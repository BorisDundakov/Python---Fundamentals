numbers_line = input()
n_removes = int(input())
numbers_list = numbers_line.split()
integer_map = map(int, numbers_list)
integer_list = list(integer_map)
print(integer_list)
counter = 0
for index in range(len(numbers_list)):
    for i in range(n_removes):
        numbers_list.remove(i)
print(integer_list)
