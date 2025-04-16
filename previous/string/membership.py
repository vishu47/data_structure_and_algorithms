def findVowel():
    lst = "wfef235AJBDnKEIfbKUAHUIA"
    count = 0
    for i in lst:
        if i in "aeiouAEIOU":
            count += 1
    print(count)


findVowel()
