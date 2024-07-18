from copy import deepcopy

# multi level of copy called deep copy
a = [4, 5, 3, [1, 7, 6, 5], 9, 100]
b = deepcopy(a)  # deep copy
print(id(a))
print(id(b))
b[3][0] = 100
print(a)
print(b)


# shallow copy
a = [4, 5, 3, 1, 7, 6, 5, 9, 100]
# # one level of copy
# b = a.copy()  # shallow copy
# print(id(a))
# print(id(b))

# pass by reference
# def printing_ref(lst):
#     lst[1] = 100


# a = [4, 5, 3, 1, 7, 6, 5, 9, 100]
# print(a)
# printing_ref(a)
# print(a)


# a = [4, 5, 3, 1, 7, 6, 5, 9, 100]

# for i in range(0, len(a)):
#     if a[i] % 2 == 0:
#         a[i] = a[i] + 1
#     a[i] = a[i] - 1

# print(a)

# print(a)

# a[1] = 20
# a[-1] = 200

# print(a)
