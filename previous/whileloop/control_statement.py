"""
continue
break
while True
"""


def KeepAsking() -> None:
    while True:
        inp = int(input("Ask Number : "))
        if inp == 0:
            break


KeepAsking()
