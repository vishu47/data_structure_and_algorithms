class Recatangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

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
area = m.area()
print(area)
sq = m.isSqure()
print(sq)
pr = m.perimeter()
print(pr)
m.updateSides(9, 9)
area = m.area()
print(area)
sq = m.isSqure()
print(sq)
pr = m.perimeter()
print(pr)
