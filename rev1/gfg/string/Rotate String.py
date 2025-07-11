def RotateString():
    s1  = "mightandmagic"
    s2 = "andmagicmigth"
    
    f = ""
    f = s1 + s1
    ind = f.find(s2)

    if ind == -1:
        return False
    return True
    
    
print(RotateString())