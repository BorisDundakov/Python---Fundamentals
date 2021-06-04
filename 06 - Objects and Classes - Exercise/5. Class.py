class Class:
    __students_count = 22

    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if Class.__students_count > len(self.students):
            self.students.append(str(name))
            self.grades.append(float(grade))

    def get_average_grade(self):
        average_grade = sum(self.grades) / len(self.students)
        return round(average_grade, 2)

    def __repr__(self):
        return f"The students in {self.class_name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
