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


ss = "maynameisvishnuAI"
replaceConsonants(ss)
