secret_message = input().split()

digits = ""
digits_list = []
letters = ""
letters_list = []

for each_word in secret_message:
    for each_letter in each_word:
        if each_letter.isdigit():
            digits += each_letter
            if letters != "":
                letters_list.append(letters)
                letters = ""

        elif not each_letter.isdigit():
            digits_list.append(digits)
            digits = ""
            letters += each_letter

for el in digits_list:
    if not el.isdigit():
        digits_list.remove(el)
    if el == '':
        digits_list.remove(el)

final = [int(el) for el in digits_list]

for el in final:
    print(chr(el))

print(letters_list)