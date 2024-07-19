from typing import List


# def totalCountOfEvenAndOdd(lst: List):
#     odd = 0
#     even = 0
#     for num in lst:
#         if num % 2 != 0:
#             odd += 1
#         else:
#             even += 1
#     print(f"count of odd : {odd}")
#     print(f"count of even : {even}")


# def totalCount(lst: List):
#     sum = 0
#     for num in lst:
#         if num % 2 != 0:
#             sum += num
#     print(sum)


# def printPrimeNumber(lst: List):
#     for num in lst:
#         flag = True
#         for i in range(2, num):
#             print(num, "lll")
#             if num % i == 0:
#                 flag = False
#                 break
#         if flag:
#             print(f"Number is Prime : {num}")


# def printListOfPrimeNumber(lst: List):
#     flag = True
#     result = []
#     for num in lst:
#         for i in range(2, num):
#             if num % i == 0:
#                 flag = False
#                 break
#         if flag:
#             print(num)
#             result.append(num)
#     print(f"prime number list : {result}")


# def sumOfAllPrimeNumber(lst: List):
#     sum = 0
#     for num in lst:
#         flag = True
#         for i in range(2, num):
#             if num % i == 0:
#                 flag = False
#                 break
#         if flag:
#             sum += num
#     print(f"Sum of all prime numbers : {sum}")


# def devisibleBy5InReverse(lst: List):
#     result = []
#     for num in lst:
#         if num % 5 == 0:
#             result.append(num)

#     # reverse resulted list
#     result.reverse()
#     print(result)


# def findTheMaxNumber(lst: List):
#     maxx = lst[1]
#     for num in lst:
#         if num > maxx:
#             maxx = num
#     print(f"Maximum number  : {maxx}")


# def findTheMinNumber(lst: List):
#     maxx = lst[1]
#     for num in lst:
#         if num < maxx:
#             maxx = num
#     print(f"Minimum number  : {maxx}")


def largestPrimeNumber(lst: List):
    mxPrime = float("-inf")
    for num in lst:
        flag = True
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break
        if flag:
            print(num, mxPrime)
            if num > mxPrime:
                mxPrime = num
    print(f"Max Prime number : {mxPrime}")


mylist = [7, 11, 23, 101, 25, 47, 32, 54]
# largestPrimeNumber(mylist)
# findTheMinNumber(mylist)
# findTheMaxNumber(mylist)
# devisibleBy5InReverse(mylist)
# sumOfAllPrimeNumber(mylist)
# printListOfPrimeNumber(mylist)
# printPrimeNumber(mylist)
# totalCount(mylist)
# totalCountOfEvenAndOdd(mylist)
