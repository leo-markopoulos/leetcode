def findLengthOfLCIS(nums):
    result = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] <= nums[j - 1]:
                break
            result = max(result, j - i)
    return result + 1