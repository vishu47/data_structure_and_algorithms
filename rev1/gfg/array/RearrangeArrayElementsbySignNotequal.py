def RearrangeArrayElementsbySignNotequal():
    # arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
    arr = [9,4,-2,-1,5,0,-5,-3,2]
    # arr = [1,2,-4,-5]
    
    
    pos = []
    neg = []
    for i in range(0 , len(arr)):
        if arr[i] > 0 :
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    
    
    print(pos,neg,len(pos),len(neg))
    if len(pos) > len(neg):
        for i in range(0, len(neg)):
            arr[i*2] = pos[i]
            arr[i*2 + 1] = neg[i]
            
        # index from where till pos and neg are filled so
        index = len(neg) * 2
        for i in range(len(neg), len(pos)):
            arr[index] = pos[i]
            index+=1
    else:
        for i in range(0, len(pos)):
            arr[i*2] = pos[i]
            arr[i*2 + 1] = neg[i]
            
        # index from where till pos and neg are filled so
        index = len(pos) * 2
        for i in range(len(pos), len(neg)):
            arr[index] = neg[i]
            index+=1
        
    return arr
        
            
print(RearrangeArrayElementsbySignNotequal())