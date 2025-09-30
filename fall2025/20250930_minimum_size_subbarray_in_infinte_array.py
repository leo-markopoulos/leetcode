def minSizeSubarray(nums, target):
    extra = 0 
    if sum(nums) < target:
        extra = target // sum(nums) * len(nums)
        target -= target // sum(nums) * sum(nums)
        if target == 0:   
            return extra
    nums += nums
    result = float('inf')
    current = 0
    left = 0
    for right in range(len(nums)):
        current += nums[right]
        while right - left + 1 > len(nums)//2:
            current -= nums[left]
            left += 1
        while current >= target:
            if current == target:
                result = min(result, right - left + 1)
            current -= nums[left]
            left += 1

    return result + extra if result != float('inf') else -1