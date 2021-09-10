# # # squares = {1: 1, 2: 4, 3: 9}
# # #
# # # for each_key in squares.keys():
# # #     print(each_key, end=" ")
# #
# #
# # squares = {1: "Ferrari", 2: "Lamborghini", 3: "McLaren"}
# #
# # for (key, value) in squares.items():
# #     print(f"Key: {key}, Value: {value}")
#
#
# # my_dict = {1: "Hello", 2: "World"}
# #
# # new_dict = my_dict.copy()
# #
# # new_dict.clear()
# # print(my_dict)
# # print(new_dict)
#
#
# pop_dict = {1: "Hello", 7: "World"}
# pop_dict.pop(7)
# print(pop_dict)

dict = {1: 'a', 2: '', 3: 'b', 4: '', 5: '', 6: 'c'}
for key, value in list(dict.items()):
    if (value == ''):
        del dict[key]
print(dict)