import sys
is_Valid = False
number = float(input())


for i in range(0, sys.maxsize):
    if 1 <= number <= 100:
        is_Valid = True
        break
    else:
        number = float(input())

if is_Valid:
    print(f"The number {number} is between 1 and 100")
