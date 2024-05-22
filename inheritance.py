class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def walk(self):
        print(f"{self.name} is walking.")

    def talk(self):
        print(f"{self.name} is talking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year, gpa):
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa

    def study(self):
        print(f"{self.name} is studying.")

    def attend_class(self):
        print(f"{self.name} is attending class.")

    def write_exam(self):
        print(f"{self.name} is writing an exam.")

class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def grade_students(self):
        print(f"{self.name} is grading students.")

    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")

# Creating objects
student = Student("John Doe", 20, "CID123", "S001", "Computer Science", 2, 3.8)
teacher = Teacher("Jane Smith", 35, "CID456", "Mathematics", 5000, "Science", "Professor")

# Accessing attributes and calling methods
print(f"Student Name: {student.name}")
print(f"Student ID: {student.student_id}")
student.study()
student.attend_class()
student.write_exam()

print("\n")

print(f"Teacher Name: {teacher.name}")
print(f"Teacher Subject: {teacher.subject}")
teacher.teach()
teacher.grade_students()
teacher.attend_meeting()