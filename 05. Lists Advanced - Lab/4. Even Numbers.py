# numbers_as_int = [int(el) for el in input().split(", ")]
# final_list = []
# for el in range(len(numbers_as_int)):
#    if numbers_as_int[el] % 2 == 0:
#        final_list.append(el)

# print(final_list)
final_list = []
numbers_as_int = [int(el) for el in input().split(", ")]


def even_numbers(numbers_list):
    for el in range(len(numbers_list)):
        if numbers_list[el] % 2 == 0:
            final_list.append(el)

    print(final_list)


even_numbers(numbers_as_int)