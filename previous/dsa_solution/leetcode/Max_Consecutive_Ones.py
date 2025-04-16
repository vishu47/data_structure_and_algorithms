def findMaxConsecutiveOnes(nums: list[int]) -> int:
    large = 0
    maxi = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            maxi += 1
            large = max(maxi, large)
        else:
            maxi = 0

    return large


a = [1, 0, 1, 1, 0, 1]
cc = findMaxConsecutiveOnes(a)
print(cc)
