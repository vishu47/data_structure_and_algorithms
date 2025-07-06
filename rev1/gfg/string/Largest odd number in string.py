def Largestoddnumberinstring():

    # s = "504"
    # s = "2042"
    s = "41839"
    
    maxi = -1
    track = ""
    
    for i in s:
        track += i
        num = int(track)
        if num % 2 != 0:
            maxi = max(maxi , num)
    
    if maxi == -1 :
        return ""
    return maxi 


print(Largestoddnumberinstring())
