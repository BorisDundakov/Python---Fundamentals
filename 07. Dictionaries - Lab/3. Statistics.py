input_dict = {}
command = input()
while command != "statistics":
    initial_input = command.split(": ")
    product = initial_input[0]
    quantity = int(initial_input[1])

    if product in input_dict:
        input_dict[product] += quantity
        command = input()
        continue

    input_dict[product] = quantity

    command = input()

print("Products in stock:")
for (key, value) in input_dict.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(input_dict.keys())}")
print(f"Total Quantity: {sum(input_dict.values())}")
