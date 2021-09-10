word_sequence = input().lower().split()
dictionary = {}

for each_word in word_sequence:
    # going through each word entry

    if each_word not in dictionary:

        dictionary[each_word] = 0
    dictionary[each_word] += 1

for (key, value) in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")
