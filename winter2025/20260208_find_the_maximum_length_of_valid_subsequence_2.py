def maximumLength(nums, k):
    dp = [[0] * k for _ in range(k)]  
    result = 0
    for num in nums:
        current_rem = num % k
        for prev_rem in range(k):
            dp[prev_rem][current_rem] = dp[current_rem][prev_rem] + 1
            result = max(result, dp[prev_rem][current_rem])
    return result