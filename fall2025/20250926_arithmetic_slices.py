def numberOfArithmeticSlices(nums):
    result = 0
    left = 0
    for right in range(2,len(nums)):
        if nums[right] - nums[right-1] != nums[right-1] - nums[right-2]:
            left = right - 1
        else:
            result += max(0, right-left-1)
    return result