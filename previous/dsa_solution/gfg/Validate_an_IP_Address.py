def isValid(str):
    sp = str.split(".")

    if len(sp) != 4:
        return False

    for num in sp:
        # check if num is number and not empty
        if not num.isdigit():
            return False

        if len(num) > 1 and num[0] == "0":
            return False

        if int(num) < 0 or int(num) > 255:
            return False

    return True


stt = "222.111.111.111"
# stt = "5555..555"
# stt = "255..255.255"
# stt = "01.01.01.01"
cc = isValid(stt)
print(cc)
