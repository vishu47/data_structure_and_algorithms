def Anagram():

    s1 = "geeks" 
    s2 = "kseeg"
    # s1 = "bc" 
    # s2 = "ad"
    
    # sort and compare
    print(sorted(s1))
    print()
    
    if "".join(sorted(s1)) == "".join(sorted(s2)):
        return True
    else:
        return False
    
    
    # mp = {}
    
    # if len(s1) != len(s2):
    #     return False
    
    # for i in s1:
    #     if i in mp:
    #         mp[i] = mp[i] + 1
    #     else:
    #         mp[i] = 1
    # print(mp)
    
    # for j in s2:
    #     if j in mp:
    #         if mp[j] == 0:
    #             return False
    #         else:
    #             mp[j] = mp[j] - 1
    #     else:
    #         return False
    
    # return True

print(Anagram())