def maximumTop(nums, k):
    if len(nums) == 1:
        return -1 if k % 2 == 1 else nums[0]
    elif k <= 1:
        return nums[k]
    elif k < len(nums):
        return max(max(nums[:k-1]), nums[k])
    elif k < len(nums) + 2: 
        return max(nums[:k-1])
    return max(nums)