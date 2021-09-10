command = input()
my_dict = {}
while command != "End":
    split_command = command.split("-")
    importance = int(split_command[0])
    string = split_command[1]

    my_dict[importance] = string

    command = input()

a = dict(sorted(my_dict.items()))

final = list(a.values())

print(final)