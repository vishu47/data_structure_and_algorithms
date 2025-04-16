def rotate(nums: list[int], k: int) -> None:
    # left = nums[: len(nums) - k]
    # right = nums[len(nums) - k :]
    # for i in range(len(right)):
    #     nums[i] = right[i]
    # for i in range(len(left)):
    #     nums[i + k] = left[i]

    # optimal
    # it gives the points where we slice even after length is less than k
    # print(D, nums[D + 1 :], nums[: D + 1])
    D = k % len(nums)
    print(nums[:-D], nums[-D:])
    nums[:] = nums[D:] + nums[:D]

    print(nums)


a = [1, 2, 3, 4, 5, 6, 7]
l = 3
rotate(a, l)
