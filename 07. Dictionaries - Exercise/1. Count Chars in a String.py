text = input()
my_dict = {}
quantity = 1

for element in text:
    if element not in my_dict:
        if element == " ":
            continue
        my_dict[element] = quantity
    else:
        my_dict[element] += 1

for key, value in my_dict.items():
    print(f"{key} -> {value}")
