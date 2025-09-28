def maximumUniqueSubarray(nums):
    seen = set()
    left = 0
    current = 0
    result = 0
    for right in range(len(nums)):
        while nums[right] in seen:
            seen.remove(nums[left])
            current -= nums[left]
            left += 1
        seen.add(nums[right])
        current += nums[right]
        result = max(result, current)
    return result