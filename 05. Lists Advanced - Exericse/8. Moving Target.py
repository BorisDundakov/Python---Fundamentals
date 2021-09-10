target_sequence = [int(el) for el in input().split()]

command = input()

while command != "End":
    split_command = command.split()
    type_command = split_command[0]
    index_command = split_command[1]
    power_command = split_command[2]

    for individual_target in range(len(target_sequence)):

        if type_command == "Shoot":
            if int(index_command) <= len(target_sequence):
                target_sequence[int(index_command)] -= int(power_command)
                if target_sequence[int(index_command)] <= 0:
                    target_sequence.remove(target_sequence[int(index_command)])

        elif type_command == "Add":
            if int(power_command) <= len(target_sequence):
                target_sequence.insert(int[index_command], int[power_command])
            else:
                print("Invalid placement!")

        elif type_command == "Strike":
            if int(index_command) <= len(target_sequence):
                target_sequence.remove(target_sequence[int(index_command)])
            else:
                print("Strike missed!")
                continue

    command = input()

print(target_sequence)
