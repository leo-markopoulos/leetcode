def maxFrequency(nums, k):
    result = 0
    for i in range(1, 51):
        if i == k:
            continue
        current = max_current = 0
        for num in nums:
            if num == i:
                current += 1
            elif num == k:
                current -= 1
            current = max(current, 0)
            max_current = max(max_current, current)
        result = max(result, max_current)
    return  nums.count(k) + result