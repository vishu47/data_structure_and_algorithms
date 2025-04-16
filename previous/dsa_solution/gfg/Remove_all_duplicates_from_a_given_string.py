def removeDuplicates(str):
    res = ""
    for i in range(len(str)):
        if str[i] not in res:
            res += str[i]
    return res


st = "cacbbcCCBc"
# cabCB
cc = removeDuplicates(st)
print(cc)
