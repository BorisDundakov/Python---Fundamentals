total_submissions_count = 0
command = input()
exam_dict = {}
language_dict = {}
while command != "exam finished":
    initial_input = command.split("-")

    username = initial_input[0]
    language = initial_input[1]

    if language not in language_dict:
        language_dict[language] = [username]
    else:
        language_dict[language].append(username)

    if language != "banned":
        points = int(initial_input[2])
        if username not in exam_dict:
            exam_dict[username] = [points]
            total_submissions_count += 1

            command = input()
            continue
        else:
            if exam_dict[username] < [points]:
                exam_dict[username] = [points]

            command = input()
            continue

    else:
        username = initial_input[0]
        del exam_dict[username]
        total_submissions_count += 1

    command = input()

print("Results:")
key_sorted_dict = dict(sorted(exam_dict.items(), key=lambda x: x[0].lower()))

value_sorted_dict = dict(sorted(key_sorted_dict.items(), key=lambda x: x[1], reverse=True))

for key, value in (value_sorted_dict.items()):
    print(f"{key} | {''.join([str(f) for f in value])}")

print("Submissions:")

key_sorted_language_dict = dict(sorted(language_dict.items(), key=lambda x: x[0].lower()))
value_sorted_language_dict = dict(sorted(key_sorted_language_dict.items(), key=lambda x: x[1]))

for keys, values in value_sorted_language_dict.items():
    if keys == "banned":
        continue
    print(f"{keys} - {len(values)}")
