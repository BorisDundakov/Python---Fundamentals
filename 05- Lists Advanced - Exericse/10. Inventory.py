items_list = input().split(", ")
command = input()

while command != "Craft!":
    split_command = command.split(" - ")
    type_command = split_command[0]
    item = (split_command[1])

    if type_command == "Collect":
        if item not in items_list:
            items_list.append(split_command[1])

    elif type_command == "Drop":
        if item in items_list:
            items_list.remove(item)

    elif type_command == "Combine Items":
        split_combination = item.split(":")

        old_item = split_combination[0]
        new_item = split_combination[1]

        for old_item_index in range(len(items_list)):
            if items_list[old_item_index] == old_item:
                items_list.insert(old_item_index + 1, new_item)

    elif type_command == "Renew":
        if item in items_list:
            items_list.remove(item)
            items_list.append(item)

    command = input()

# final_output = ", ".join(items_list)
# print(final_output)
# print(f"Default item list == {items_list}")

print(*items_list, sep=", ")
