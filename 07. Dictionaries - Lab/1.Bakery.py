initial_input = input().split()
products = {}
quantity = 0

for element in range(0, len(initial_input), 2):
    product = initial_input[element]
    quantity += 1
    products[product] = quantity
    #dictname[key] = value

print(products)
