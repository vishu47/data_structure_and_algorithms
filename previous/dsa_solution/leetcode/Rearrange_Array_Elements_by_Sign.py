def rearrangeArray(nums: list[int]) -> list[int]:
    # n = []
    # p = []
    # for i in nums:
    #     if i < 0:
    #         n.append(i)
    #     else:
    #         p.append(i)
    # print(n, p)

    # i = 0
    # j = 0
    # while i < len(p):
    #     nums[j] = p[i]
    #     j += 2
    #     i += 1
    # k = 0
    # l = 1
    # print(nums)
    # while k < len(n):
    #     nums[l] = n[k]
    #     l += 2
    #     k += 1

    # print(nums)

    # n = []
    # p = []
    # for it in nums:
    #     if it < 0:
    #         n.append(it)
    #     if it >= 0:
    #         p.append(it)

    # print(n, p)
    # for i in range(len(p)):
    #     nums[2 * i] = p[i]
    #     nums[2 * i + 1] = n[i]
    # print(nums)
    # return []

    res = [0] * len(nums)
    p, n = 0, 1
    for i in range(len(nums)):
        if nums[i] >= 0 and p < len(nums):
            res[p] = nums[i]
            p += 2
        else:
            res[n] = nums[i]
            n += 2

    print(res)
    return []


a = [3, 1, -2, -5, 2, -4]
cc = rearrangeArray(a)
print(cc)
