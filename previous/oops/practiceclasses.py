class MyHome:
    def __init__(
        self,
        name: str,
        age: int,
        address: str,
        gender: str,
        bills: int,
        education: int,
        grocery: int,
    ):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.education = education
        self.grocery = grocery
        self.bills = bills

    def spends(self):
        total = self.bills + self.grocery + self.education
        return f"total spend is : {total}"

    def spendBreakdown(self):
        return f"Education spend is : {self.education} \nGroceries spend is : {self.grocery} \nBills spend is : {self.bills} \n "

    def personalDetails(self):
        return f"name is {self.name} and age near about {self.age} and lives in {self.address}"


cad1 = MyHome(
    name="vishun",
    address="jamoliya",
    gender="male",
    age=23,
    bills=456,
    education=678,
    grocery=100,
)

personalDeatils = cad1.personalDetails()
print(personalDeatils)
cadSpends = cad1.spends()
print(cadSpends)
spendBreakdown = cad1.spendBreakdown()
print(spendBreakdown)
