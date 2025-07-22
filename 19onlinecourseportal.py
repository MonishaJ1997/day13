# Student class
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return f"{self.name} (ID: {self.student_id})"


# Instructor class
class Instructor:
    def __init__(self, name, expertise):
        self.name = name
        self.expertise = expertise

    def __str__(self):
        return f"{self.name}, Expert in {self.expertise}"


# Base Assignment class (with submit method to be overridden)
class Assignment:
    def __init__(self, title):
        self.title = title

    def submit(self):
        return f"Submitting assignment: {self.title}"


# Subclasses demonstrating polymorphism
class Quiz(Assignment):
    def submit(self):
        return f"Quiz '{self.title}' submitted with MCQ answers."


class Project(Assignment):
    def submit(self):
        return f"Project '{self.title}' uploaded with ZIP file."


class Essay(Assignment):
    def submit(self):
        return f"Essay '{self.title}' submitted as a PDF document."


# Course class (Aggregation)
class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.instructor = None
        self.assignments = []

    def enroll_student(self, student):
        self.students.append(student)

    def assign_instructor(self, instructor):
        self.instructor = instructor

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def show_course_info(self):
        print(f"📘 Course: {self.name}")
        print(f"👩‍🏫 Instructor: {self.instructor}")
        print("👨‍🎓 Enrolled Students:")
        for s in self.students:
            print("  ", s)
        print("📝 Assignments:")
        for a in self.assignments:
            print("  -", a.title)

# Create students and instructor
s1 = Student("Meena", "ST101")
s2 = Student("Ravi", "ST102")
inst = Instructor("Dr. Arun", "Machine Learning")

# Create assignments
quiz = Quiz("Week 1 Quiz")
project = Project("ML Mini Project")
essay = Essay("Ethics in AI")

# Create course
course = Course("AI Fundamentals")
course.enroll_student(s1)
course.enroll_student(s2)
course.assign_instructor(inst)
course.add_assignment(quiz)
course.add_assignment(project)
course.add_assignment(essay)

# Display course info
course.show_course_info()

# Simulate submission
print("\n📤 Submissions:")
for a in course.assignments:
    print("-", a.submit())
