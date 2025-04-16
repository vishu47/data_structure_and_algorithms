ss = "maynameisvishnuAI"


def reverseString(st):
    print(st[::-1])


# reverseString(ss)


def upperCaseString(st):
    print(ss.upper())


# upperCaseString(ss)


def removeALlVowels(st):
    x = st.lower()
    print("".join(ch for ch in x if ch not in "aeiou"))


# removeALlVowels(ss)


def countWords(st):
    counts = 0
    for i in st:
        if i == " ":
            counts += 1
    print(counts + 1)


# ss = "this is good and better new time and live in shahar"
# countWords(ss)


def longestWord(st):
    long = ""
    curr = ""
    for i in st:
        if i == " ":
            if len(curr) > len(long):
                long = curr
            curr = ""
        else:
            curr = curr + i

    # edge case
    if len(curr) > len(long):
        long = curr
    print(long)


ss = "this is good and better new time and live in shahar "
# longestWord(ss)


def capitalizedString(st):
    sp = False
    sss = ""
    for i in range(len(st) - 1):
        if sp:
            sp = False
            continue
        if st[i] == " " and st[i + 1] != " ":
            csp = chr(ord(st[i + 1]) - 32)
            sss += " " + csp
            sp = True
        elif i == 0:
            csp = chr(ord(st[i]) - 32)
            sss += csp
        else:
            sss += st[i]

    print(sss)


# ss = "this is good and better  new time and live in shahar "
# capitalizedString(ss)


def replaceConsonants(st):
    sss = st.lower()
    aa = ""
    for i in sss:
        if i not in "aeiou":
            aa += "*"
        else:
            aa += i

    print(aa)


# ss = "maynameisvishnuAI"
# replaceConsonants(ss)


def removeNonAlphabatics(st):
    l = st.lower()
    f = ""
    for i in l:
        x = ord(i)
        if x >= 97 and x <= 122:
            f += i
    print(f)


# ss = "mayn#am$e%#is@#@ish%#%nu@@!!AI"
# removeNonAlphabatics(ss)


def countChar(st):
    f = 0
    for i in st:
        if i >= "0" and i <= "9":
            f += 1
    print(f)


# ss = "78g67"
# countChar(ss)


def removeDuplicate(st):
    f = ""
    for i in st:
        if i not in f:
            f += i
    print(f)


ss = "egerggergergregregerg"
# removeDuplicate(ss)


def replaceSpacesWith(st):
    # x = ss.replace(" ", "-")
    f = ""
    for i in st:
        if i == " ":
            f += "-"
        else:
            f += i
    print(f)


ss = "this is vishnu maurya"

replaceSpacesWith(ss)
