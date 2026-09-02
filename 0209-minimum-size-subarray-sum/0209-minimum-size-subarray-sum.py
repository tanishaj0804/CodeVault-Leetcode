class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        minv = float('inf')
        s = 0
        i = j = 0
        while j<len(nums):
            s += nums[j]
            while s >= target:
                minv = min(minv,j-i+1)
                s -= nums[i]
                i += 1
            j += 1
        return minv


        