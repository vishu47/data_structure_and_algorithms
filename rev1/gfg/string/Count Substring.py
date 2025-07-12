def CountSubstring():
    s = "abcabc"
    mp = {}
    st = ""
    
    for i in s:
        mp[i] = mp.get(i , 0 ) + 1 
        
    print(mp)
    
    
    
    
print(CountSubstring())