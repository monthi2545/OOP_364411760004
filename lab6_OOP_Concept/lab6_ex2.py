class Student:
    def __init__(self):
        self.name = ""
        self.major = ""
        self.gpa = ""

    # display object attribute
    def student_info(self):
        print(f'name:{self.name} major:{self.major} gpa {self.gpa}')


s1 = Student() # empty object
# assing data to object attribute
s1.name = "MON"
s1.major = "MIT"
s1.gpa = 3.0

# display student data
s1.student_info()

# get data form user
# s2 = Student()
# s2.name = input("Enter name:")
# s2.major = input("Enter major:")
# s2.gpa = float(input("Enter GPA"))
# s2.student_info()

std = []

n = int(input('How many Student? :  '))
for i in range(n):
    s = Student()
    print(f"Please,enter info {i+1}:")
    s.name = input("Enter name:")
    s.major = input("Enter major:")
    s.gpa = float(input("Enter GPA"))
    std.append(s)

# display all student in list
for i in std:
    i.student_info()
