n_pairs = int(input())
student_grade_dict = {}

for i in range(n_pairs):
    student_name = input()
    student_grade = float(input())

    if student_name not in student_grade_dict:
        student_grade_dict[student_name] = []
        # defining that the values in student_grade_dict will be stored in a list

    student_grade_dict[student_name].append(student_grade)

filtered_grades = {}

for student_name, grades in student_grade_dict.items():
    avg_grade = sum(grades) / len(grades)
    if avg_grade >= 4.5:
        filtered_grades[student_name] = avg_grade


sorted_best_students = sorted(filtered_grades.items(), key=lambda kvp: -kvp[1])
# -kvp[1] works for NUMBERS only {returns them in reverse}
#
# sorted_best_students = sorted(filtered_grades.items(), key=lambda kvp: kvp[1], reverse = True)

# sorted връща лист от tuples, затова няма нужда да пиша sorted_best_students.items()

for student_name, grade in sorted_best_students:
    print(f"{student_name} -> {grade :.2f}")

