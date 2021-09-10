numbers_line = [el for el in input().split()]
numbers_line.sort(reverse=True)
numbers_as_string = "".join(numbers_line)
print(numbers_as_string)

print(sorted(numbers_line, reverse=True))


