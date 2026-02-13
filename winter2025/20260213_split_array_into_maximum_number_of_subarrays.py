def maxSubarrays(nums):
    mx = 1048575 
    ans, acc = 0, mx
    for num in nums:
        acc&= num
        if acc == 0 :
            ans+= 1 
            acc = mx
    return 1 if ans == 0 else ans 