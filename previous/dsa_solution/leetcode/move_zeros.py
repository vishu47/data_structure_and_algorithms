def moveZeroes(nums: list[int]) -> None:
    # not preserving position
    # i = 0
    # j = len(nums) - 1
    # while i < j:
    #     if nums[i] == 0:
    #         nums[i], nums[j] = nums[j], nums[i]
    #         i += 1
    #         j -= 1
    #     else:
    #         i += 1
    # print(nums)

    # nonz = 0
    # for i in range(len(nums)):
    #     if nums[i] != 0:
    #         nums[nonz] = nums[i]
    #         nonz += 1
    # for j in range(nonz, len(nums)):
    #     nums[j] = 0

    # print(nums)

    l = 0
    r = 0
    for i in range(len(nums)):
        # if nums[i] == 0: this line gives all zeros on starting preserving all 
        if nums[i] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r += 1
        else:
            r += 1

    print(nums)


a = [0, 1, 0, 3, 12]
moveZeroes(a)
