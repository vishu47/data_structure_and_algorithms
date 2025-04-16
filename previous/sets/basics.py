# mutable
# pass by reference will work bcz it will change in origin set
# set will take ony hashable data eg : int,tuple,string
# unique unordered

# myset = {2, 4, 6, 7, 4, 4, 3, 4, 4, 5, 5, "Vishnu", 9.99}
# print(myset) #unordered

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7, 8}
# set3 = set1 + set2
# set3 = set1 / set2
# set3 = set1 % set2
# print(set1 - set2)  # items in a not in b
# print(set2 - set1)  # items in b not in 1


# print(set1.)
set1.add(100)  # add at random position
set1.remove(100)  # add at random position
# set1.clear()  # return None
# print(set1)

# newset1 = set1
# print(newset1)
# print(set1)
newset1 = set1.copy()
newset1.add(1000)
print(newset1)
print(set1)
