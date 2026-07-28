class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        ans = float('inf') 
        l = 0
        s = 0
        if target in nums:
            return 1
        if sum(nums) < target:
            return 0
        for i in range(len(nums)):
            s += nums[i]
            while s >= target:
                ans = min(ans,i-l+1)
                s -= nums[l]
                l+=1
        return ans
        