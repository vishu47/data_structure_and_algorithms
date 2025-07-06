def ReverseWordsinaString():
    S = " i like this program very much"
    word = ""
    arr = []
    ans = ""
    for i in range(0, len(S)):
        if S[i] == " " :
            if word !== "":
                arr.append(word)  
                word = ""
        
        else:
            word += S[i] 
            
            if i == len(S) - 1:
                arr.append(word)  

    for i in range(len(arr) - 1 , -1 , -1):
        ans += arr[i] + " " 
    
    return ans
    
print(ReverseWordsinaString())

