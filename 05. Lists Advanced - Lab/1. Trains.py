n_wagons = int(input())

zeroes_list = ["0" * n_wagons]
print(zeroes_list)

command = input().split()
for element in range(len(zeroes_list)):
    while command != "End":
        action = command[0]

        if action == "add":
            zeroes_list[::-1] += command[::-1]
            print(zeroes_list)
        elif action == "insert":
            pass
        elif action == "leave":
            pass

        command = input()

    print(zeroes_list)
    break
