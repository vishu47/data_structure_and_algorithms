def productExceptSelf(nums):
    l = len(nums)
    left = [1] * l
    right = [1] * l

    for lt in range(l):
        left[lt] = nums[lt]

    print(left)

    # prod = 1
    # zero = 0
    # p = []
    # for num in nums:
    #     if num > 0:
    #         prod *= num
    #     else:
    #         zero += 1

    # for i in range(len(nums)):
    #     if zero > 1:
    #         p.append(0)
    #     elif zero == 1:
    #         if arr[i] == 0:
    #             p.append(prod)
    #         else:
    #             p.append(0)
    #     else:
    #         p.append(prod // arr[i])

    # return p


arr = [1, 2, 3, 4, 5]
# arr = [1, 0]
cc = productExceptSelf(arr)
print(cc)
