def sumRecursion(x):
    ss = 0
    if x <= 0:
        return x
    if x % 2 == 0:
        print(x)
        ss = sumRecursion(x - 1)
    return x + ss


x = int(input("Eneter number :"))
c = sumRecursion(x)
print(c)
