number = int(input())
counter = 0
symbol = "*"
for number in range(number):
    counter += 1
    print(symbol * counter)

for number in range(number, 0, -1):
    counter -= 1
    print(symbol * counter)
