def signleAmongsDouble():
    arr = [1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65]
    sig = 0
    for i in range(0 , len(arr)):
        sig = sig ^ arr[i]
        print(sig)
    return sig
    
print(signleAmongsDouble())