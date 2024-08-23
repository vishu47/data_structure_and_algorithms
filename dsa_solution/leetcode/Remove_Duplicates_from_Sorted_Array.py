def removeDuplicates(nums: list[int]) -> int:
    # num = {}
    # for i in range(len(nums)):
    #     num[nums[i]] = 0
    # j = 0
    # for key in num:
    #     nums[j] = key
    #     j += 1

    # return j

    i = 0
    j = i + 1
    if len(nums) == 1:
        return 1

    while j < len(nums):
        if nums[i] != nums[j]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        j += 1
    return i + 1


a = [1, 1, 2]
cc = removeDuplicates(a)
print(cc)
