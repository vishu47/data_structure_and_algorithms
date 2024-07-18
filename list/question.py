lst = [34, 54, 22, 34, 33, 31, 37, 89, 90, 65, 7]

# list comprehensive methods
# odd = [lst[i] for i in range(len(lst)) if lst[i] % 2 != 0]
# print(odd)


def UpdateElemInList(lst):
    for i in range(0, len(lst)):
        if lst[i] % 2 != 0:
            lst[i] = lst[i] + 1
    print(lst)


UpdateElemInList(lst)


# def AskUser(length: int) -> list[int]:
#     lst = []
#     for i in range(length):
#         a = int(input("add nuumber : "))
#         lst.append(a)
#     return lst


# a = int(input("ask length : "))
# print(AskUser(a))
