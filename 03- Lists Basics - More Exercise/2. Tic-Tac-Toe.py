first_row = input().split()
second_row = input().split()
third_row = input().split()

integer_first_row = list(map(int, first_row))
integer_second_row = list(map(int, second_row))
integer_third_row = list(map(int, third_row))

print(integer_first_row)
print(integer_second_row)
print(integer_third_row)

winner = False

for i in range(len(first_row)):
    if integer_first_row[i] == integer_second_row[i] == integer_third_row[i] and integer_first_row != 0:
        winner = True
        break

    elif integer_first_row[i] == integer_second_row[i - 1] == integer_third_row[i - 2] and integer_first_row != 0:
        winner = True
        break

    elif integer_first_row[i] == integer_first_row[i - 1] == integer_first_row[i - 2] and integer_first_row != 0:
        winner = True
        break

    elif integer_second_row[i] == integer_second_row[i - 1] == integer_second_row[i - 2] and integer_second_row != 0:
        winner = True
        break

    elif integer_third_row[i] == integer_third_row[i - 1] == integer_third_row[i - 2] and integer_third_row != 0:
        winner = True
        break

    else:
        winner = False
        break

if winner:
    print("We have a winner!")

if not winner:
    print("Draw!")