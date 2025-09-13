def rotate(nums, k):
    nums[:] = nums[-k % len(nums):] + nums[:-k % len(nums)]