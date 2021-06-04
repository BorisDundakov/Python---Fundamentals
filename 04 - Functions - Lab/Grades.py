def grade_function(grade_parameter):
    if 2.00 <= grade_parameter <= 2.99:
        return "Fail"
    elif 3.00 <= grade_parameter <= 3.49:
        return "Poor"
    elif 3.50 <= grade_parameter <= 4.49:
        return "Good"
    elif 5.50 <= grade_parameter <= 6.00:
        return "Excellent"

    # ако една функция няма успешен return, връща None

entered_grade = float(input())

result = grade_function(entered_grade)
print(result)
