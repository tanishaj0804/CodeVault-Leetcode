class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums:
            return 1
        if sum(nums) < target:
            return 0
        l = r = 0
        sumv = 0
        minl = float('inf')
        while r < len(nums):
            sumv += nums[r]
            while sumv >= target:
                minl = min(minl,r-l+1)
                sumv -= nums[l]
                l += 1
            r += 1
        return minl


        