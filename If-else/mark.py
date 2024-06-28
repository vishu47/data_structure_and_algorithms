a = int(input(f"marks : "))

if a > 1 and a < 60:
    print("fail")
elif a > 61 and a <= 70:
    print("D")
elif a > 71 and a <= 80:
    print("C")
elif a > 81 and a <= 90:
    print("B")
elif a > 91 and a <= 100:
    print("A")
