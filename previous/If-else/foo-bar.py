a = int(input(f"marks : "))

if a % 3 == 0 and a % 5 == 0:
    print("FOOBAR")
elif a % 3 == 0:
    print("FOO")
elif a % 5 == 0:
    print("BAR")
else:
    print("Invalid")
