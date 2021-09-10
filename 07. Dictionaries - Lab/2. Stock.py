# products_list = input().split()
# looked_for_products = input().split()
# final_product_dict = {}
#
# for element in range(0, len(products_list), 2):
#     product = products_list[element]
#     quantity = int(products_list[element + 1])
#     final_product_dict[product] = quantity
#
# print(final_product_dict)
# for element in range(len(looked_for_products)):
#     for (key, value) in final_product_dict.items():
#         if looked_for_products[element] in final_product_dict:
#             print(f"We have {final_product_dict[element]} of {looked_for_products[element]} left.")
#             break
#
#     else:
#         print(f"Sorry, we don't have {looked_for_products[element]}")


elements = input().split()
bakery = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    bakery[key] = int(value)

searched_products = input().split(" ")
for product in searched_products:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")