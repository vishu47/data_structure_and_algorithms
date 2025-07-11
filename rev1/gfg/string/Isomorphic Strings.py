def IsomorphicStrings():
    # s1 = "aab"
    # s2 = "xxy"
    # s1 = "aab"
    # s2 = "xyz"
    s1 = "abc"
    s2 = "xxz"
    
    
    mp = {}
    
    for i in range(len(s1)):
        if s1[i] in mp:
            if mp[s1[i]] == s2[i]:
                continue
            else:
                return False
        else:
            
            if s2[i] in mp.values():
                return False
            mp[s1[i]] = s2[i]

    return True
    

print(IsomorphicStrings())