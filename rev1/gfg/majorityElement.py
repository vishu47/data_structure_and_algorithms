def majorityElement():
    arr = [7]
    mp = {}
    for i in arr:
        if i in mp:
           mp[i] = mp[i] + 1
        else:
            mp[i] = 1
    n = len(arr)//2
    f = -1
    for [key , val] in mp.items():
        if val > n:
            return key
    
print(majorityElement())