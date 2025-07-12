def ImplementAtoi():
    
    
    # s = "-123"
    s = "-999999999999"
    # s = "  -0012gfg4"
    # s = "  -"
    # s = "123"
    
    
    sign = 1 # posive by default for negative it will be -1
    i = 0
    sum = 0
    
    while i < len(s):
        if s[i] == " ":
            i+=1
        else:
            break
            
    if s[i] == "-":
        sign = -1
        i+=1
        
        
    # print("kj".isnumeric())
    while i < len(s) and s[i].isnumeric():
        # print(s[i])
        sum = sum * 10 + int(s[i])
        print(sum > 2**31,sum)
        if sum*sign > 2**31:
            return 2**31 - 1
        elif sum*sign < -2**31:
            return -2**31
        
        i += 1
        
    return sum * sign


print(ImplementAtoi())