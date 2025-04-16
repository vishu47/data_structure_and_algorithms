def greet():
    print(f"greet")
    callme()


def callme():
    print(f"callme")
    greet()


# greet()
# callme()


def avg():
    a = int(input("number one : "))
    b = int(input("number two : "))
    c = int(input("number three : "))
    avg = (a + b + c) / 3
    print(avg)


def avg_with_arg(
    b: int,
    c: int,
    a: int = 0,
):
    avg = (a + b + c) / 3
    print(avg)


def avg_with_arg_default(a=3, b=10, c=10):
    avg = (a + b + c) / 3
    print(avg)


def marks(science: int, hindi: int, math: int, geography: int, english: int):

    avg = (science + hindi + math + geography + english) / 5
    per = ((science + hindi + math + geography + english) / 500) * 100
    print(f"Percentage : {per} and avg {avg}")


def defaultParams(science: int, hindi: int, math: int, geography: int, english: int):

    avg = (science + hindi + math + geography + english) / 5
    per = ((science + hindi + math + geography + english) / 500) * 100
    print(f"Percentage : {per} and avg {avg}")


# print()


avg()
# avg_with_arg(2, 3, 4)
# avg_with_arg_default()
# marks(20, 30, 40, 60, 40)
# avg_with_arg(10, 20) # optional should be right hand side and optional should be left hand side
# defaultParams(20, 30, 40, 60, 40)
# defaultParams(geography=20, hindi=30, science=40, english=60, math=40)
