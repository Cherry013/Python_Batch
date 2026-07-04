class Student:
    """Just a student class"""
    total = 0
    def  __init__(self, name, age):
        self.name = name
        self.age = age
        Student.total +=1

    def display(self, phno,Branch):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Branch: {Branch}")
        print(f"Phone: {phno}")
        self.total_students()

    @classmethod
    def total_students(cls):
        print(f"Total Students: {cls.total}")

    @classmethod
    def change(cls,n):
        cls.total = n

    @staticmethod
    def just(name, age):
        if len(name) < 10 and age < 18:
            print("Name too short and age must be greater than 18")
        else:
            print("Valid credentials")



s1 = Student("John", 25)
s2 = Student("Michael", 35)
s3 = Student("Bob", 35)

s1.display(2345678,"CSE")
print()
Student.display(s1,5678998765,"CSE")
Student.total_students()
Student.change(20)
s1.change(25)
s1.total_students()
Student.total_students()
Student.just("Michael", 35)
s1.just("Michael", 20)

s1.total += 1
print(s1.total)
print(s2.total)
print(s3.total)
print(Student.total)

print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)

print(Student.__dict__)




class Student:
    passing_marks = 40
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= Student.passing_marks:
            print(f"{self.name} : pass")
        else:
            print(f"{self.name} : fail")

    @classmethod
    def update(cls,pm):
        cls.passing_marks = pm

    @staticmethod
    def grade_category(m):
        if m >= 90:
            return "A"
        elif m >= 80:
            return "B"
        elif m >= 70:
            return "C"
        elif m >= 60:
            return "D"
        else:
            return "F"


s1 = Student("Jaya simha", 99)
s2 = Student("sohail", 98)
s3 = Student("Ganesh", 35)
s4 = Student("RK", 96)

s1.result()
s2.result()
s3.result()
s4.result()

s3.update(99)
s1.marks = 9
s3.marks = 100
s1.result()
s2.result()
s3.result()
s4.result()


print(s1.grade_category(s1.marks))