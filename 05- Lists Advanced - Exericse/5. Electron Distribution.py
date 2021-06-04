# import math
#
# number_of_electrons = int(input())
# electrons_list = [0]
#
# for shell in range(1, number_of_electrons + 1):
#     maximum = int(2 * (math.pow(shell, 2)))
#     electrons_list.append(shell)
#     while electrons_list[shell] < maximum and sum(electrons_list) < number_of_electrons:
#             electrons_list[shell] += 1
#     if sum(electrons_list) >= number_of_electrons:
#         break
#
# electrons_list.remove(electrons_list[0])
# print(electrons_list)

number_of_electrons = int(input())
electrons = []
shell_number = 1

while number_of_electrons > 0:
    max_electrons_in_current_shell = 2 * shell_number ** 2
    if max_electrons_in_current_shell > number_of_electrons:
        electrons.append(number_of_electrons)
    else:
        electrons.append(max_electrons_in_current_shell)
    number_of_electrons -= max_electrons_in_current_shell
    shell_number += 1

print(electrons)