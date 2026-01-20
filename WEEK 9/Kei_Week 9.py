import newRunner

# ------------------ Using class from module ------------------
student_obj = newRunner.Student(
    name="Kei Dimac",
    grade=1.00,
    subject=["Physics", "Chemistry"]
)
student_obj.print_student_info()

# ------------------ Local Student Class ------------------
class Student:
    def __init__(self, student_name, student_grade, student_subjects):
        self.student_name = student_name
        self.student_grade = student_grade
        self.student_subjects = student_subjects

    def print_student_info(self):
        print(
            f"Name: {self.student_name} | "
            f"Grade: {self.student_grade} | "
            f"Subjects: {self.student_subjects}"
        )

    @staticmethod
    def is_grade_passing(grade):
        return grade <= 3.0


if __name__ == "__main__":

    student1 = Student("Jan Vincent Guardian", 1.00, ["Physics", "Chemistry"])
    student1.print_student_info()
    print("Passed" if Student.is_grade_passing(student1.student_grade) else "Failed")

student1_name = "Ashe"
student1_grade = "1.5"
student1_subject = ["Algebra", "Physics"]

student2_name = "Keith"
student2_grade = "1.6"
student2_subject = ["Geometry", "Physics"]

