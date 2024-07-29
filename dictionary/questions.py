lst = [3, 4, 5, 6, 7, 6, 6, 6, 6, 5, 4, 4, 3, 3, 4, 5, 6, 67, 78, 8, 7, 6, 5, 5]


def msxFreq(lst):
    dic = {}
    for i in lst:
        dic[i] = dic.get(i, 0) + 1
    print(dic)

    max_fre = 0
    max_elem = 0
    for key in dic:
        if dic[key] > max_fre:
            max_fre = dic[key]
            max_elem = key

    print(f"{max_fre}: {max_elem}")


# msxFreq(lst)


def stringFreq():
    ss = "ahgghgtzzhjsklhhhgaaaaaauaa"
    dic = {}
    for i in ss:
        dic[i] = dic.get(i, 0) + 1

    print(dic)


# stringFreq()


def detalsDictMarks(dic):
    # for key, val in dic.items():
    #     sum = 0
    #     for i in val:
    #         sum += i
    #     print(f"{key} has scored {sum}")
    max_mar = 0
    max_name = 0
    for key in dic:
        sum = 0
        for i in range(len(dic[key])):
            sum += dic[key][i]

        if sum > max_mar:
            max_mar = sum
            max_name = key

    print(f"{max_name} has scored {max_mar}")


details = {
    "Anirudh": [56, 78, 65, 45, 90],
    "Sanjay": [58, 78, 56, 12, 33],
    "Muskan": [87, 78, 65, 45, 80],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40, 65, 63, 54],
}
detalsDictMarks(details)
