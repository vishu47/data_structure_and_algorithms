def makeSubjectMarksDict(x):
    dic = {}
    i = 0
    while i < x:
        sub = input("Enter subject name : ")
        marks = int(input(f"Enter marks {sub} : "))
        a = {sub: marks}
        dic[sub] = marks
        i += 1
    print(dic)


# x = int(input("Enter number of subjects :"))
# makeSubjectMarksDict(x)


def frequncyCounter(lst):
    dic = {}
    for num in lst:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    print(dic)


ls = [4, 5, 6, 5, 4, 4, 7]
# frequncyCounter(ls)


def mergeTwoListInDict(lst1, lst2):
    dic = {}
    for i in range(len(lst1)):
        dic[lst1[i]] = lst2[i]
    print(dic)


ls1 = ["hindi", "english", "maths", "sci"]
ls2 = [34, 45, 45, 78]
# mergeTwoListInDict(ls1, ls2)


def findKeyInDict(key):
    dic = {"hindi": 34, "english": 45, "maths": 45, "sci": 78}
    return key in dic


# k = input("Enter Key Name : ")
# print(findKeyInDict(k))


def updateDict():
    dic1 = {"apple": 3, "banana": 5, "cherry": 7}
    dic2 = {"banana": 8, "orange": 10, "apple": 9}
    dic3 = {}
    for key, value in dic1.items():
        dic3[key] = value
    for key, value in dic2.items():
        dic3[key] = value

    print(dic3)


# updateDict()


def updateWithMultiplyIfValueNumber(n):
    dic = {"a": 3, "b": "Vishnu", "c": True, "d": 9}
    for key, value in dic.items():
        if type(value) == int:
            dic[key] = value * n
    print(dic)


# x = int(input("Enter the multiplicatiion number : "))
# updateWithMultiplyIfValueNumber(x)


def updateKeyAndValue():
    main = {}
    for i in range(1, 50):
        main[i] = i
    # print(main)

    res = {}
    for key, val in main.items():
        if int(key) > 0 and int(key) < 16:
            res[key] = val**2
    print(res)


# updateKeyAndValue()


def returnOnlyStringKeys():
    dic = {"a": 3, "b": "Vishnu", "c": True, "d": 9}
    dicc = {}
    for key, val in dic.items():
        if type(val) == str:
            dicc[key] = val
    print(dicc)


returnOnlyStringKeys()
