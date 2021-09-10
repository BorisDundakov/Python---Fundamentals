rage_input = input()
unique_symbols_counter = 0
my_dict = {}

full_list = []
l_list = []
final = ""

for letter in rage_input:
    if letter.upper() not in full_list and not letter.isdigit():
        full_list.append(letter.upper())

for el in range(0, len(rage_input)):
    if not rage_input[el].isdigit():
        if rage_input[el] not in l_list:
            l_list.append(rage_input[el])
            unique_symbols_counter += 1

    else:
        integer_value = int(rage_input[el])
        final += "".join(l_list) * integer_value
        # print(final.upper(), end="")
        l_list.clear()
        integer_value = 0

    continue

print(f"Unique symbols used: {len(full_list)}")
print(final.upper(), end="")