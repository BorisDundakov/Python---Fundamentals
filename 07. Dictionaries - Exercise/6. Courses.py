command = input()
dictionary = {}
while command != "end":
    split_command = command.split(" : ")
    course_name = split_command[0]
    student_name = split_command[1]
    if course_name not in dictionary:
        # in order to be able to append new values later
        # you need to save the original value in an array

        dictionary[course_name] = [student_name]
    else:
        dictionary[course_name].append(student_name)

    command = input()
# print(dictionary.values())
for key in dictionary:
    for k in sorted(dictionary, key=lambda k: len(dictionary[k]), reverse=True):

        print(f"{k}: {len((dictionary.get(k)))} ")
        sorted_dict = sorted(list(dictionary.get(k)))

        for el in sorted_dict:
            print(f"-- {el}")
    break
