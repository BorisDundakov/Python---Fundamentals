first_list = input().split(", ")
second_list = input().split(", ")
final_list = []


for i in range(len(first_list)):
    for j in range(len(second_list)):
        if first_list[i] in second_list[j]:
            final_list.append(first_list[i])
            break

print(final_list)
