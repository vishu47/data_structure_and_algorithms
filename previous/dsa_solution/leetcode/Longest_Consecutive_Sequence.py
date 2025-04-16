def longestConsecutive(nums: list[int]) -> int:
    # count = 1
    # long = 1
    # nums.sort()
    # print(nums)
    # for i in range(len(nums) - 1):
    #     if nums[i + 1] == nums[i] + 1:
    #         count += 1
    #     else:
    #         long = max(long, count)
    #         count = 1
    # return max(long, count)

    # broot
    def linearS(arr, item):
        for it in arr:
            if it == item:
                return True
        return False

    long = 1
    for it in nums:
        count = 1
        x = it
        while linearS(nums, x + 1) == True:
            count += 1
            x += 1
        long = max(long, count)

    return long


a = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1, 1, 2, 2, 2, 1, 1, 1]
cc = longestConsecutive(a)
print(cc)
