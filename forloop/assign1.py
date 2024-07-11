n = int(input())
print("------------------------------------------")

for i in range(1, n + 1):
    for j in range(i, n + 1):
        print(j, end=" ")
    print()

# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5


# for i in range(1, n + 1):
#     for j in range(i, n + 1):
#         print(j, end=" ")
#     print()

# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5

# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1


# for i in range(n, 0, -1):
#     for j in range(n, i - 1, -1):
#         print(j, end=" ")
#     print()

# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

# for i in range(1, n):
#     for j in range(n - i, n + 1):
#         print(j, end=" ")
#     print()

# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5
