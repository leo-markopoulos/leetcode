def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0      
    result = 0
    total = 1
    left = 0
    for right in range(len(nums)):
        total *= nums[right]
        while total >= k:
            total //= nums[left]
            left += 1
        result += right - left + 1
    return result