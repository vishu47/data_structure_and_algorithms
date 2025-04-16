# defult it will run str magic method and without it it will print the address


class Recatangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"length : {self.length} width : {self.width}"

    def area(self):
        return self.length * self.width

    def isSqure(self):
        return self.length == self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def updateSides(self, length, width):
        self.length = length
        self.width = width


m = Recatangle(4, 5)
n = Recatangle(8, 9)
print(m)
print(n)
