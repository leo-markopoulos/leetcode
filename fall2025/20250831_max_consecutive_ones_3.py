def longestOnes(nums, k):
    left = 0
    result = 0
    zeroes = 0
    for right in range(len(nums)):

        if nums[right] == 0:
            zeroes += 1

        while zeroes > k:
            if nums[left] == 0:
                zeroes -= 1
            left += 1

        result = max(result, right-left+1)
    return result