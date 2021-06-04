line_of_words = input().split()
searched_palindrome = input()
palindrome_counter = 0
palindrome_list = []

for i in range(len(line_of_words)):
    potential_reverse_word = line_of_words[i]
    if potential_reverse_word == potential_reverse_word[::-1]:
        palindrome_list.append(potential_reverse_word)

    if searched_palindrome == line_of_words[i]:
        palindrome_counter += 1

print(palindrome_list)
print(f"Found palindrome {palindrome_counter} times")
