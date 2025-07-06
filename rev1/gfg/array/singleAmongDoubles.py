def singleAmongDoubles():
    arr = [2, 2, 5, 5, 20, 30, 30]
    xor = 0
    
    for i in arr:
        xor = xor ^ i
        
    return xor

# https://www.geeksforgeeks.org/problems/element-appearing-once2552/1?_gl=1*13h4zks*_up*MQ..&gclid=CjwKCAjwiezABhBZEiwAEbTPGJ4AEditFZnVdy_9pNcIaN-CHlv_tiYTFczaZY1XXT6fWY7X081ncBoCH7AQAvD_BwE&gbraid=0AAAAAC9yBkDlkmH0JZGsRiiyy-pPEqC0H
print(singleAmongDoubles())