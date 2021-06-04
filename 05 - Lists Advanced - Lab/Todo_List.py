command = input()
to_do_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_to_do = [10]
while command != "End":
    split_command = command.split("-")
    importance = int(split_command[0])
    command_type = split_command[1]
    to_do_list[importance] = command_type
    command = input()

for el in range(len(to_do_list)+1):
    try:
        int(el)
        to_do_list.remove(el)

    except:
        pass

print(to_do_list)
