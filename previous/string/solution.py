# find the longest words in string


def longestWord(lst):
    long = ""
    curr = ""
    for i in lst:
        if i == " ":
            if len(curr) > len(long):
                long = curr
            curr = ""
        else:
            curr = curr + i
    if len(curr) > len(long):
        long = curr

    print(long)


mylist = "python is the most easy language and this is great llllllllllllllll"
longestWord(mylist)
