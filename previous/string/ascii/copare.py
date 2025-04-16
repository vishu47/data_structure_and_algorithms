def removeAll():
    my_string = "a%b@c9d_e.f"
    newStr = ""
    for i in my_string:
        x = ord(i)
        if x >= 97 and x <= 122:
            newStr += chr(x)
    print(newStr)


# removeAll()

#
# def makeUpperToLowerAndLowerToUpper():
#     my_string = "DHhdjka^&#$(*)$   ...///;;''DADWAHKjyuihdwakj"
#     newStr = ""
#     for i in my_string:
#         x = ord(i)
#         if x >= 97 and x <= 122:
#             newStr = newStr + chr(x - 32)
#         elif x >= 65 and x <= 90:
#             newStr = newStr + chr(x + 32)
#         else:
#             newStr = newStr + chr(x)
#     print(newStr)


# makeUpperToLowerAndLowerToUpper()


def askChar():
    my_string = ""
    # ch = input("Enter Character : ")
    # if ord(ch) == ord("q"):
    #     print(my_string)
    # else:
    #     askChar()
    # my_string += ch

    while True:
        ch = input("Enter Character : ")
        if ord(ch) == ord("q") or ord(ch) == ord("Q"):
            break
        my_string += ch


# askChar()


# def CountSymbols(my_string):
#     num = 0
#     alp = 0
#     ALP = 0
#     space = 0
#     symbols = 0
#     for ch in my_string:
#         ascii_code = ord(ch)
#         if ascii_code >= 97 and ascii_code <= 122:
#             alp += 1
#         elif ascii_code >= 65 and ascii_code <= 90:
#             ALP += 1
#         elif ascii_code >= 49 and ascii_code <= 57:
#             num += 1
#         elif ascii_code == 32:
#             space += 1
#         else:
#             symbols = len(my_string) - (alp + space + num)
#     print(alp, ALP, num, space, symbols)


# my_string = "dhaw43789HGDSAK&*(#$  HDK486/*-+daw)"
# CountSymbols(my_string)

# def islower(user_string: str) -> bool:
#     is_lower = False
#     is_upper = False
#     for ch in user_string:
#         ascii_code = ord(ch)
#         if ascii_code >= 97 and ascii_code <= 122:
#             is_lower = True
#         elif ascii_code >= 65 and ascii_code <= 90:
#             is_upper = True
#     # if is_lower == True and is_upper == False:
#     #     return True
#     if is_lower and not is_upper:
#         return True
#     return False


# my_string = "djwakplL57439&%$(*)%"
# islower(my_string)

# count = 0
# count1 = 0
# for i in my_string:
#     x = ord(i)
#     if x >= 65 and x <= 90:  # capital letters
#         count += 1
#     elif x >= 97 and x <= 122:  # small letters
#         count1 += 1
# print(count, count1)


# for i in my_string:
#     if ord("A") >= ord(i) and ord(i) <= ord("Z"):  # capital letters
#         count += 1
#     elif ord(i) >= ord("a") and ord(i) <= ord("z"):  # small letters
#         count1 += 1
# print(count, count1)
