from abc import ABC, abstractmethod

# Abstract base User class
class User(ABC):
    def __init__(self, username):
        self.username = username

    @abstractmethod
    def show_dashboard(self):
        pass

# Question class with encapsulated answer
class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.__correct_answer = correct_answer  # private

    def check_answer(self, user_answer):
        return user_answer.strip().lower() == self.__correct_answer.strip().lower()

    def display(self):
        print(f"Q: {self.text}")
        for i, opt in enumerate(self.options, start=1):
            print(f"  {i}. {opt}")

# Exam class
class Exam:
    def __init__(self, title):
        self.title = title
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def conduct_exam(self):
        score = 0
        for q in self.questions:
            q.display()
            ans = input("Your answer: ").strip()
            if q.check_answer(ans):
                score += 1
        return score

# Admin class
class Admin(User):
    def __init__(self, username):
        super().__init__(username)
        self.exams = []

    def create_exam(self, title):
        exam = Exam(title)
        self.exams.append(exam)
        return exam

    def show_dashboard(self):
        print(f"\n🛠️ Admin Dashboard ({self.username})")
        print("Available Exams:")
        for i, exam in enumerate(self.exams, start=1):
            print(f"  {i}. {exam.title}")

# Student class
class Student(User):
    def __init__(self, username):
        super().__init__(username)
        self.scores = {}

    def show_dashboard(self):
        print(f"\n📚 Student Dashboard ({self.username})")
        if self.scores:
            print("Results:")
            for exam, score in self.scores.items():
                print(f"  {exam}: {score}")
        else:
            print("No exams taken yet.")

    def take_exam(self, exam):
        print(f"\n📝 Starting Exam: {exam.title}")
        score = exam.conduct_exam()
        self.scores[exam.title] = f"{score}/{len(exam.questions)}"
        print(f"✅ Exam Completed! Score: {score}/{len(exam.questions)}")
# Admin creates exam
admin = Admin("admin01")
exam1 = admin.create_exam("Python Basics")

# Add questions
exam1.add_question(Question("What is the output of 2+2?", ["3", "4", "5"], "4"))
exam1.add_question(Question("What data type is []?", ["list", "tuple", "dict"], "list"))

# Student appears for exam
student = Student("ravi123")

# Admin dashboard
admin.show_dashboard()

# Student dashboard before exam
student.show_dashboard()

# Conduct exam
student.take_exam(exam1)

# Student dashboard after exam
student.show_dashboard()

