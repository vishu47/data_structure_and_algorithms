def PassingMarks(
    science: int, hindi: int, math: int, geography: int, english: int
) -> bool:

    per = ((science + hindi + math + geography + english) / 500) * 100

    # if per < 33:
    #     return False
    # return False

    return per >= 33


a = PassingMarks(10, 23, 21, 23, 43)
print(a)
