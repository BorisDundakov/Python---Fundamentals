starting_point = int(input())
ending_point = int(input())
for asci in range(starting_point, ending_point + 1, +1):
    letter = chr(asci)
    print(letter, end=" ")

