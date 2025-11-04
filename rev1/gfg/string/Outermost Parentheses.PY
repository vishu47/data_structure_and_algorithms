def OutermostParentheses():
    # s = "(()())(())"
    s = "((()())(())(()(())))"
    stack = []
    print(len(stack) == 0)
    count = 0
    st = ""
     
    for i in s:
        if i == "(" :
            if len(stack) == 0:
                stack.append(i)
            else:
                st += i
                stack.append(i)
                
        else:
            stack.pop()
            if len(stack) == 0:
                continue
            else:
                st += i
            
        return st
                

print(OutermostParentheses())