class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if target in nums:
            return 1
        if target > sum(nums):
            return 0
        l = 0
        s = 0
        ans = float('inf')
        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                ans  = min(ans,r-l+1)
                s -= nums[l]
                l+=1
        return ans 




        