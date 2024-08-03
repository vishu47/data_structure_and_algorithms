class Student:
    def __init__(self, roll_no: int, name: str, age: int, gender: str, marks=[]):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender
        self.marks = marks

    def updateStudent(self, new_name=None, age=None, gender=None) -> None:
        if new_name:
            self.name = new_name
        if age:
            self.age = age
        if gender:
            self.name = gender

    def total(self) -> int:
        # return sum(self.marks)
        t = 0
        for m in self.marks:
            t = t + m
        return t

    def display(self):
        print(f"Rol No = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")
        print(f"marks = {self.marks}\n\n")


# students_data = [
#     Student(1, "Anirudh", 55, "Male", [56, 45, 21, 46, 99]),
#     Student(2, "Nihar", 11, "Male", [56, 90, 15]),
# ]
# students_data[1].display()
# print(students_data[0].marks)
# print(students_data[0].name)
# print(students_data[1].total())
# print(students_data[1].age)

student_list = []


def addMarksInList(n: int):
    marks = []
    i = 0
    while i <= n - 1:
        x = int(input(f"subject {i} :"))
        marks.append(x)
        i += 1
    return marks


def findStudent():
    x = int(input("Enter the roll number: "))
    # else will run when for loop run on whole list meand not found
    for stu in student_list:
        if stu.roll_no == x:
            stu.display()
            break
    else:
        print("Student is not available on the database \n\n")


while True:
    print("1) Add a student")
    print("2) Remove a student")
    print("3) Display student details")
    print("4) Update student details")
    print("5) Exit")
    print("6) Total marks")
    print("7) Search a student by roll number : ")
    choice = int(input("Enter your choice = "))
    if choice == 1:
        roll_no = int(input("Enter roll_no: "))
        name = input("Enter name: ")
        age = int(input("Enter age : "))
        gender = input("Enter gender : ")
        n = int(input("Number of subjects : "))
        marks = addMarksInList(n)
        x = Student(roll_no, name, age, gender, marks)
        student_list.append(x)
        print(student_list)
    elif choice == 2:
        x = int(input("Enter the student roll no. for deletion : "))
        index = -1
        for stu in student_list:
            index = student_list.index(stu)

        if index == -1:
            print("Student is not available")
        else:
            student_list.pop(index)
        print(student_list)

    elif choice == 3:
        if not student_list:
            print("No studnet list")
        for i in student_list:
            i.display()
        pass
    elif choice == 4:
        x = int(input("Enter the roll number: "))
        # else will run when for loop run on whole list meand not found
        for stu in student_list:
            if stu.roll_no == x:
                name = input("Enter New Student Name : ")
                age = input("Enter New Student Age : ")
                gender = input("Enter New Student Gender : ")
                stu.updateStudent(name, age, gender)
                stu.display()
                break

    elif choice == 5:
        break
    elif choice == 6:
        pass
    elif choice == 7:
        findStudent()
    else:
        print("Invalid Choice")
