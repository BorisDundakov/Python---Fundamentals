number = int(input())
word = input()
list_of_strings = []
filtered_list = []

for _ in range (number):
    string_input = input()
    list_of_strings.append(string_input)

    if word in string_input:
        filtered_list.append(string_input)

print(list_of_strings)
print(filtered_list)