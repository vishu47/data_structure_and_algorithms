class Student:
    # attribute/class variables
    id = 0
    name = ""
    address = ""
    gender = ""
    age = 0
    adult = ""

    def setDetails(self):
        self.id = int(input("Enter ID : "))
        self.name = input("Enter name : ")
        self.address = input("Enter address : ")
        self.age = input("Enter age : ")
        self.adult = input("Enter adult : ")
        self.gender = input("Enter gender : ")

    def display(self):
        print(f"self.id : {self.id}")
        print(f"self.name : {self.name}")
        print(f"self.age : {self.age}")
        print(f"self.address : {self.address}")
        print(f"self.gender : {self.gender}")
        print(f"self.adult : {self.adult}")


s1 = Student()
s2 = Student()
# print(s1)  # address
# s1.address = "jamoliya"
# s1.id = 1
# s1.name = "vishnu"
# s1.gender = "male"
# s2.address = "jamoliya"
# s2.id = 2
# s2.name = "kumari"
# s2.gender = "female"
# print(f"s1.name : {s1.name}")  # address
# print(f"s1.gender : {s1.gender}")  # address
# print(f"s2.name : {s2.name}")  # address
# print(f"s2.gender : {s2.gender}")  # address


s1.setDetails()
print("")
s1.display()
