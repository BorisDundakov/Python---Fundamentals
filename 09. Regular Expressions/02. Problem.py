import re

request_list = []
n = int(input())
request_dict = {}
pattern = r"^(\$|\%)(?P<tag>[A-Z][a-z]{2,})\1\:\s\[(?P<uppercase_letter>[0-9]{1,})\]\|\[(?P<char_two>[0-9]{1,})\]\|\[(?P<char_three>[0-9]{1,})\]\|$"
numbers_list = []
for el in range(n):
    text = input()
    answer = re.findall(pattern, text)
    # print(answer)
    if not answer:
        print("Valid message not found!")
    else:
        for ind_el in answer:
            for a in range(len(ind_el)):
                if a == 1:
                    request_list.append(ind_el[a])
                elif a > 1:
                    numbers_list.append((chr((int(ind_el[a])))))

            # print(request_list)
            # print(numbers_list)

            print(f"{''.join(request_list)}: {''.join(numbers_list)}")


            request_list.clear()
            numbers_list.clear()
#
# print(request_dict)
