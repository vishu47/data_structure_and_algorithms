def buyandselllstocks():
    arr = [100, 180, 260, 310, 40, 535, 695]
    pr = 0
    buy = arr[0]
    
    for i in range(0, len(arr)):
        dif = arr[i] - buy
        
        pr = max(pr,dif)
        
        buy = min(buy , arr[i])
            
        
    return pr

print(buyandselllstocks())
    