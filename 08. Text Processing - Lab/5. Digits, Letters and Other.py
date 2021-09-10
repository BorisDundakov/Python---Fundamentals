line = input()
digits = []
letters = []
others = []

for el in line:
    if el.isdigit():
        digits.append(el)
    elif el.isalpha():
        letters.append(el)
    else:
        others.append(el)

print("".join(digits))
print("".join(letters))
print("".join(others))