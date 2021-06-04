data = input()

# nested dictionary solution

products = {}

while not data == "buy":
    name, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products.keys():
        products[name] = {"product_price": price, "product_quantity": quantity}

    else:
        products[name]["product_quantity"] += quantity

        products[name]["product_price"] = price

    data = input()

for key, value in products.items():
    result = value["product_price"] * value["product_quantity"]
    print(f"{key} -> {result :.2f}")
