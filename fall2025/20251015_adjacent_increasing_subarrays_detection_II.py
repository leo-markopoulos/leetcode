class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return 0

        best = 0
        prev_run = 0
        curr_run = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_run += 1
            else:
                best = max(best, min(prev_run, curr_run), curr_run // 2)

                prev_run = curr_run
                curr_run = 1
                
        best = max(best, min(prev_run, curr_run), curr_run // 2)
        
        return best