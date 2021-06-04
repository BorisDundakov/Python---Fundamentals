text = input()
final_output = []

for each_letter in range(0, len(text)):
    if each_letter not in final_output:
        if text[each_letter] != text[each_letter - 1] or each_letter == 0:
            final_output.append(text[each_letter])

print("".join(final_output))
