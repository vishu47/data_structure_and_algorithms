def consecutiveones():
    # arr = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
    # arr = [1, 1, 0, 0, 1, 1, 1, 0]
    arr = [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    f = 0
    fo = 0
    max = 0
    maxo = 0
    
    for i in arr:
        if i == 1:
            max += 1
            if max > f:
                f = max
        else:
            max = 0
            
        if i == 0:
            maxo += 1
            if maxo > fo:
                fo = maxo
        else:
            maxo = 0
           
           
    if f > fo:
        return f
    
    return fo 

# https://www.geeksforgeeks.org/find-element-appears-array-every-element-appears-twice/?_gl=1*s5afbz*_up*MQ..&gclid=CjwKCAjwiezABhBZEiwAEbTPGJ4AEditFZnVdy_9pNcIaN-CHlv_tiYTFczaZY1XXT6fWY7X081ncBoCH7AQAvD_BwE&gbraid=0AAAAAC9yBkDlkmH0JZGsRiiyy-pPEqC0H
print(consecutiveones())