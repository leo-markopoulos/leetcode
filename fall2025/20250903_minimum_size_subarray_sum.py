def minSubArrayLen(target, nums):
    if sum(nums) < target:
        return 0
        
    left = 0
    result = len(nums)
    total = 0
    for right in range(len(nums)):

        total += nums[right]

        while total - nums[left] >= target:
            total -= nums[left]
            left += 1

        if total >= target:
            result = min(result, right-left+1)

    return result     