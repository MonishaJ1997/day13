# Base class
class Person:
    def __init__(self, name, person_id):
        self._name = name
        self._id = person_id

    def __str__(self):
        return f"{self._name} (ID: {self._id})"

# Subject class
class Subject:
    def __init__(self, name):
        self.name = name
        self.__mark = None

    def set_mark(self, mark):
        self.__mark = mark

    def get_mark(self):
        return self.__mark

    def get_grade(self):
        if self.__mark is None:
            return "Not Graded"
        elif self.__mark >= 90:
            return "A+"
        elif self.__mark >= 75:
            return "A"
        elif self.__mark >= 60:
            return "B"
        elif self.__mark >= 50:
            return "C"
        else:
            return "F"

# Student class
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
        self.__subjects = {}

    def enroll_subject(self, subject_name):
        self.__subjects[subject_name] = Subject(subject_name)

    def get_subjects(self):
        return self.__subjects

    def get_info(self):
        return f"Student: {self._name}, ID: {self._id}"

# Teacher class
class Teacher(Person):
    def __init__(self, name, teacher_id):
        super().__init__(name, teacher_id)

    def update_marks(self, student, subject_name, mark):
        subjects = student.get_subjects()
        if subject_name in subjects:
            subjects[subject_name].set_mark(mark)
            print(f"{self._name} updated {student._name}'s {subject_name} mark to {mark}")
        else:
            print("Subject not found for student.")

# ReportCard class
class ReportCard:
    def __init__(self, student):
        self.student = student

    def generate(self):
        print(f"\n📄 Report Card for {self.student._name} (ID: {self.student._id})")
        print("-" * 40)
        for subj_name, subj in self.student.get_subjects().items():
            mark = subj.get_mark()
            grade = subj.get_grade()
            print(f"{subj_name}: {mark if mark is not None else 'N/A'} → Grade: {grade}")
        print("-" * 40)


# Create students and teacher
s1 = Student("Ravi", "S001")
t1 = Teacher("Mrs. Latha", "T001")

# Enroll subjects
s1.enroll_subject("Math")
s1.enroll_subject("Science")
s1.enroll_subject("English")

# Teacher updates marks
t1.update_marks(s1, "Math", 88)
t1.update_marks(s1, "Science", 72)
t1.update_marks(s1, "English", 94)

# Generate Report Card
card = ReportCard(s1)
card.generate()
