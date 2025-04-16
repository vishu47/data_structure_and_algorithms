start = int(input("Enter Start : "))
end = int(input("End Number : "))


i = start
j = end


count = 0
while i <= j:
    if i % 7 == 0 and i % 2 == 0:
        count += 1
    i += 1
print(count)

# count = 0
# while i <= j:
#     if i % 2 == 0:
#         count += 1
#     i += 1
# print(count)

# total = 0
# while i <= j:
#     if i % 2 == 0:
#         total += i
#     i += 1
# print(total)


# if i > j:
#     i = end
#     j = start

# while i <= j:
#     print(i, end=" ")
#     i += 1

# if i > j:
#     while i >= j:
#         print(j, end=" ")
#         j += 1
# else:
#     while j >= i:
#         print(i, end=" ")
#         i += 1


# j = n
# while j <= end:
#     print(j, end=" ")
#     j += 1

# j = n
# while j <= end:
#     print(j, end=" ")
#     j += 1


# while i <= n:
#     print(i, end=" ")
#     i += 1
# print()
# print(i)
# 1 2 3 4 5
# 6


# while i <= n:
#     print(i, end=" ")
#     i += 1
