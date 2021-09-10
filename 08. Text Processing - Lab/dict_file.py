n = int(input())
synonyms_dictionary = {}

for i in range(n):
    word = input()
    synonym = input()
    if word not in synonyms_dictionary:
        # if the word(our key value) is not in the dictionary, we need to
        # create a new key value and a new list
        synonyms_dictionary[word] = []
    synonyms_dictionary[word].append(synonym)

for key, values in synonyms_dictionary.items():
    print(f"{key} - {', '.join(values)}")