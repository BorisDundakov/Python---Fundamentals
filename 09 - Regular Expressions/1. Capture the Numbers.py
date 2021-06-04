import re

text = input()
regex = r"(\d+)"

all_numbers = []

while text:
    numbers = re.findall(regex, text)
    all_numbers.extend(numbers)
    text = input()

print(*all_numbers)