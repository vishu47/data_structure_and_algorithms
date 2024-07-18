# lst = []

# for i in range(1, 101):
#     lst.append(i)

# lst = [u for u in range(1, 101)]
# lst = [i for i in range(100, 0, -1)]
# lst = [-1 for i in range(0, 5)]
# lst = [2 for i in range(0, 10)]
# lst = [0 for _ in range(0, 10)]

# add even numbers only
# lst = [i for i in range(1, 21) if i % 2 == 0]


# def is_prime_number(num: int) -> bool:
#     # I have not used factors logic here
#     # I will be explaning this in next lecture
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True


# my_list = [i for i in range(1, 101) if is_prime_number(i)]

lst = ["even" if i % 2 == 0 else "odd" for i in range(1, 20)]
lst = [f"even : {i}" if i % 2 == 0 else "odd" for i in range(1, 20)]

lst = [34, 67, 45, 32, 89, 80, 97, 94]
# ans = [num for num in lst if num % 2 == 0]
ans = [lst[i] for i in range(len(lst)) if lst[i] % 2 == 0]

print(ans)

# print(lst)
# print(my_list)
