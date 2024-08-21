def removeDuplicates(nums: list[int]) -> int:
    num = {}
    for i in range(len(nums)):
        num[nums[i]] = num.get(i, 0) + 1
    print(len(num.keys()), num)
    return len(num.keys())


a = [1, 1, 2]
removeDuplicates(a)
