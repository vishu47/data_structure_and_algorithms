def Leadersinanarray():
    # arr = [16, 17, 4, 3, 5, 2]
    # arr = [1, 2, 3, 4, 5, 2]
    # arr = [5, 10, 20, 40]
    '''
    logic :
        loop from back as last element is always leader 
        check is current element is greater than lastelement from leaders array or leaders array is empty
        reverse the leaders array
    '''
    arr = [30, 10, 10, 5]
    l = []
    for i in range(len(arr) - 1 , -1 ,-1):
        if len(l) == 0 or arr[i] >= l[-1]:
            l.append(arr[i])
            
    l.reverse()
    
    return l

print(Leadersinanarray())
                     