lst = [4, 5, 7, 4, 2, 4, 6, 7]

print(lst.sort())  # in place sorting
print(sorted(lst))  # return new sorted list


print("-".join(str(num) for num in sorted(lst)))
