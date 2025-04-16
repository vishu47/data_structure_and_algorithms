def PrintStartToEndListItem(lst, start, end):
    x = lst[start:end]
    print(x, "Sliced Lst")


def PrintTillEndListItem(lst, end):
    x = lst[len(lst) - end :]
    print(x, "Sliced Lst")


def PrintFromToNumberListItem(lst, end):
    x = lst[-1 : -end - 1 : -1]
    print(x, "Sliced Lst")


def interChangeNumber(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    print(lst)


def splitInto2Halfs(lst):
    n = len(lst)
    if n % 2 == 0:
        st = lst[: n // 2]
        nd = lst[n // 2 :]
    print(st, nd)


def generatePower(n):
    lst = [i**2 for i in range(1, n + 1)]
    print(lst)


def countDevBy3and6():
    lst = [i for i in range(1000) if i % 3 == 0 and i % 6 == 0]
    print(lst)


def countDevBy5(n):
    lst = [i for i in range(n) if i % 5 == 0]
    print(lst)


# start = int(input())
# end = int(input())
n = int(input("Enter user Number:"))
lst = [8, 5, 6, 8, 8, 4, 2, 5, 7, 5, 4, 78]
countDevBy5(n)
# countDevBy3and6()
# generatePower(n)
# PrintStartToEndListItem(lst, start, end)
# PrintTillEndListItem(lst, end)
# interChangeNumber(lst)
# splitInto2Halfs(lst)
