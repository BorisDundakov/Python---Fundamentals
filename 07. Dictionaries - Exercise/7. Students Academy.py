n_pairs = int(input())
student_grade_dict = {}

for i in range(n_pairs):
    student_name = input()
    student_grade = float(input())

    if student_name not in student_grade_dict:
        student_grade_dict[student_name] = student_grade
        continue
    else:
        student_grade_dict[student_name] += student_grade
        student_grade_dict[student_name] /= 2


for key, value in list(student_grade_dict.items()):
    if value < 4.50:
        del student_grade_dict[key]

    # noinspection PyTypeChecker
    third_grade_dict = dict(sorted(student_grade_dict.items(), key=lambda x: x[1], reverse=True))
    new_dict = third_grade_dict.copy()

# noinspection PyUnboundLocalVariable
for key, value in new_dict.items():
    print(f"{key} -> {value :.2f}")
