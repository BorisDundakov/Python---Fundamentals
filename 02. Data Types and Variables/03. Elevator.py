capacity = int(input())
n_people = int(input())

result = capacity // n_people
if result * n_people < capacity:
    result += 1
    print(result)
else:
    print(result)
