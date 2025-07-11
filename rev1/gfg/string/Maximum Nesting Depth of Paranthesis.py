def MaximumNestingDepthofParanthesis():
    
    # s = " ((5+2)(3+4)((6))) "
    s = " (43+4++3)((3)(9))+1 "
    
    cnt = 0
    ans = 0
    stack = []
    
    for i in s:
        if i == "(" :
            cnt += 1
            ans = max(ans , cnt) 
            stack.append("(")
        elif i == ")":
            cnt -= 1
            stack.pop()
            
    return ans

print(MaximumNestingDepthofParanthesis())