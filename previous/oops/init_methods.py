class Student:
    # attribute/class variables
    # these are not nessesary you cal directly assign/add during setDetails because they are object
    # id = 0
    # name = ""
    # address = ""
    # gender = ""
    # age = 0
    # adult = ""

    # it will run whenever object form Student()

    # universal  way
    def __init__(self, idd, name, address):
        self.id = idd
        self.name = name
        self.address = address

    # old way
    # def __init__(self):
    # self.id = int(input("__init__ Enter ID : "))
    # self.name = input("__init__ Enter name : ")
    # self.address = input("__init__ Enter address : ")
    # self.age = input("__init__ Enter age : ")
    # self.adult = input("__init__ Enter adult : ")
    # self.gender = input("__init__ Enter gender : ")

    def setDetails(self):
        pass
        # self.id = int(input("Enter ID : "))
        # self.name = input("Enter name : ")
        # self.address = input("Enter address : ")
        # self.age = input("Enter age : ")
        # self.adult = input("Enter adult : ")
        # self.gender = input("Enter gender : ")

    def updateName(self, name: str) -> None:
        self.name = name

    def display(self):
        print(f"self.id : {self.id}")
        print(f"self.name : {self.name}")
        print(f"self.address : {self.address}")
        # print(f"self.age : {self.age}")
        # print(f"self.gender : {self.gender}")
        # print(f"self.adult : {self.adult}")


# s1 = Student()
# s2 = Student()

# # s1.setDetails()
# s1.display()
# print("")
# # if miss to set s2 then there us default method will run which is __init__
# s2.display()

# s1 = Student(34, "vishnu", "jamoliya")
s1 = Student(
    idd=34,
    address="jamoliya",
    name="vishnu",
)
s1.updateName("Mahima")
s1.display()
