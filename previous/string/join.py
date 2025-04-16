mylist = "python is the most easy language and this is great awesome brother"

# mylist = ["v", "i", "s", "h", "n", "u"]

# print(str(mylist))  # ['v', 'i', 's', 'h', 'n', 'u']
# print(str(mylist)[0])  # [
# print(" ".join(ch for ch in mylist))
# print("".join(ch for ch in mylist))


# def reverseStr(lst):
#     x = lst.split()
#     print(x)
#     c = x[::-1]
#     com = " ".join(w for w in c)
#     print(com)


# reverseStr(mylist)


# def charReverse():
#     # method 1
#     my_string = "python is a good language"
#     x = my_string.split()
#     f = ""
#     for i in x:
#         f += i[::-1] + "-"
#     print(f[:-1])


# method 2
# print(" ".join(ch[::-1] for ch in x))


# charReverse()


def reverseByCharAndWord():
    my_string = "python is a good language"
    # egaugnal doog a si nohtyp
    # x = my_string.split()
    # l = ""
    # for i in x[::-1]:
    #     l += i[::-1] + " "
    # print(l[:-1])

    # method 2
    # words = my_string.split()
    # print(" ".join(word[::-1] for word in words[::-1]))

    # method 3
    l = ""
    for i in my_string[::-1]:
        l += l


reverseByCharAndWord()
