from abc import ABC, abstractmethod
from datetime import datetime

# Abstract Base Class
class Person(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def access_info(self):
        pass

    def __str__(self):
        return f"{self.name} ({self.gender}, {self.age})"

# Doctor class
class Doctor(Person):
    def __init__(self, name, age, gender, specialization):
        super().__init__(name, age, gender)
        self.specialization = specialization

    def access_info(self):
        return f"Dr. {self.name}, Specialist in {self.specialization}"

# Patient class
class Patient(Person):
    def __init__(self, name, age, gender, patient_id):
        super().__init__(name, age, gender)
        self.patient_id = patient_id
        self.medical_history = []

    def access_info(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}"

# Appointment class (Aggregation of Doctor and Patient)
class Appointment:
    def __init__(self, doctor, patient, date_time):
        self.doctor = doctor
        self.patient = patient
        self.date_time = date_time
        self.prescription = None

    def assign_prescription(self, prescription):
        self.prescription = prescription

    def __str__(self):
        return (
            f"\n📅 Appointment on {self.date_time.strftime('%d-%m-%Y %H:%M')}\n"
            f"👨‍⚕️ Doctor: {self.doctor.access_info()}\n"
            f"👤 Patient: {self.patient.access_info()}\n"
        )

# Prescription class
class Prescription:
    def __init__(self, medicines, instructions):
        self.date = datetime.now()
        self.medicines = medicines
        self.instructions = instructions

    def __str__(self):
        meds = "\n".join(f"- {m}" for m in self.medicines)
        return (
            f"🧾 Prescription Date: {self.date.strftime('%d-%m-%Y')}\n"
            f"Medicines:\n{meds}\nInstructions: {self.instructions}"
        )

# Create doctor and patient
doc = Doctor("Ramesh", 45, "M", "Cardiologist")
pat = Patient("Sita", 30, "F", "P123")

# Book an appointment
appt = Appointment(doc, pat, datetime(2025, 7, 25, 10, 30))

# Create and assign a prescription
pres = Prescription(["Aspirin 100mg", "Vitamin D"], "Take after meals")
appt.assign_prescription(pres)

# Print appointment and prescription
print(appt)
print(pres)
