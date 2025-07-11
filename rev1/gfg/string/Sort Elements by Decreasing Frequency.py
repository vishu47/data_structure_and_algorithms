def SortElementsbyDecreasingFrequency():
    arr = [4,6,9,19,2,16,13,11,16,17,16,8,12,16,12,18]
    mp = {}
    j = 0
    ans = []
    
    
    for i in arr:
        mp[i] = mp.get(i , 0) + 1

    print(mp.items())

    # sort list items based on fre if fre is same sort based on key in descreasing order
    
    soretedItems = sorted(mp.items() , key = lambda x : (-x[1] , x[0]))
    
    for j in soretedItems:
        
        # this line gives o(n2)
        
        # ans = ans + [i[0]]*i[1]
    
        for _ in range(j[1]):
            ans.append(j[0])
    
    print(ans)
    
print(SortElementsbyDecreasingFrequency())