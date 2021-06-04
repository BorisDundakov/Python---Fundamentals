import re

line = input()
pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-z]+-?[a-z]+(\.[a-z]+)+"

valid_variables = [obj.group() for obj in re.finditer(pattern, line)]

print(*valid_variables, sep="\n")
