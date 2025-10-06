from collections import defaultdict

def countGood(nums, k):
    freq = defaultdict(int)
    left = 0
    pairs = 0
    result = 0
    for right, char in enumerate(nums):
        pairs += freq[char]
        freq[char] += 1
        while pairs >= k:
            result += len(nums) - right
            freq[nums[left]] -= 1
            pairs -= freq[nums[left]]
            left += 1

    return result