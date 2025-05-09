def rotatearrayleftbyk():
    arr = [1,2,3,4,5]
    d = 2
    arr[:] = arr[d:] + arr[:d]
    
    return arr

print(rotatearrayleftbyk())