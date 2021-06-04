

def calculator(action):
    if action == "subtract":
        return first_num - second_num
    elif action == "add":
        return first_num + second_num
    elif action == "divide":
        return first_num // second_num
    elif action == "multiply":
        return first_num * second_num

word = input()
first_num = int(input())
second_num = int(input())

result = calculator(word)
print(result)