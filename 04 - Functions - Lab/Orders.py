def order(product_type, quantity):
    
    if product_type == "coffee":
        return quantity * 1.50
    elif product_type == "water":
        return quantity * 1.00
    elif product_type == "coke":
        return quantity * 1.40
    else:
        return quantity * 2.00


product = input()
amount = int(input())
result = order(product, amount)
print(f"{result :.2f}")
