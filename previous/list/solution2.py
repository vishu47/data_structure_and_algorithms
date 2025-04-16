from typing import List


# def copyInReversOrder() -> None:
#     myList = []
#     for _ in range(3):
#         a = int(input("Entter element : "))
#         myList.insert(0, a)
#     print(myList)


# def performAddition(lst: List[int]) -> None:
#     print(lst[1] + lst[-2])


# def removeAllEvenNumbersfromList(lst: List[int]) -> None:
#     res = []
#     for num in lst:
#         if num % 2 != 0:
#             res.append(num)
#     print(res)


# def countValueAndAdd(lst: List[int]) -> None:
#     res = []
#     for num in lst:
#         if lst.count(num) > 3:
#             if num not in res:
#                 res.append(num)
#     print(res)


# def removeNthElem(lst: List[int], index: int):
#     if len(lst) > index:
#         lst.remove(lst[index])
#     print(lst)


# def mergeListElembyElem(lst1: List[int], lst2: List[int]):
#     res = []
#     if len(lst1) == len(lst2):
#         for i in range(0, len(lst1)):
#             res.append(lst1[i] + lst2[i])
#         print(res)


def sumAndAvg(lst: List[int]):
    sum = 0
    for num in lst:
        sum += num
    print(f"sum : {sum}")
    print(f"avg : {round(sum/len(lst),2)}")


# myList = [3, 8, 7, 3, 5, 5, 5, 5, 3, 8, 3, 3, 3, 1, 3, 8, 9, 6, 7, 8, 9]
# myList1 = [3, 8, 7, 3, 5, 5, 5, 5, 3]
myList = [3, 4, 7, 9, 1, 2, 6, 3, 2]
sumAndAvg(myList)
# mergeListElembyElem(myList, myList1)
# removeNthElem(myList, 60)
# countValueAndAdd(myList)
# removeAllEvenNumbersfromList(myList)
# performAddition(myList)
# copyInReversOrder()
