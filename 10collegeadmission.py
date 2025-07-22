# Base class
class Person:
    def __init__(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact

# Department class (aggregated into Student)
class Department:
    def __init__(self, dept_name, code):
        self.dept_name = dept_name
        self.code = code

    def __str__(self):
        return f"{self.dept_name} (Code: {self.code})"

# Admission form with encapsulation
class AdmissionForm:
    def __init__(self, marks, documents):
        self.__marks = marks  # private
        self.__documents = documents  # private list of submitted docs

    def verify_documents(self):
        required_docs = {"ID Proof", "Marksheet", "Photo"}
        submitted = set(self.__documents)
        return required_docs.issubset(submitted)

    def get_marks(self):
        return self.__marks

# Student class
class Student(Person):
    def __init__(self, name, age, contact, form: AdmissionForm, department: Department):
        super().__init__(name, age, contact)  # call Person constructor
        self.form = form
        self.department = department

    def admit(self):
        if self.form.verify_documents():
            print(f"✅ Admission successful for {self.name}")
            print(f"Allocated Department: {self.department}")
            print(f"Marks Scored: {self.form.get_marks()}")
        else:
            print(f"❌ Admission failed for {self.name}: Missing documents.")

# Create Department
cs_dept = Department("Computer Science", "CS101")
mech_dept = Department("Mechanical Engineering", "ME102")

# Create Admission Forms
form1 = AdmissionForm(89.5, ["ID Proof", "Marksheet", "Photo"])
form2 = AdmissionForm(76.0, ["ID Proof", "Photo"])  # missing Marksheet

# Create Students
s1 = Student("Ravi Kumar", 18, "9876543210", form1, cs_dept)
s2 = Student("Anita Sharma", 19, "9123456780", form2, mech_dept)

# Admit Students
s1.admit()
print()
s2.admit()
