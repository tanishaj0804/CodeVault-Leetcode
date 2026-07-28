class Solution(object):
    def maximumTop(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return nums[0]
        if len(nums) == 1:
            return -1 if k % 2 else nums[0]
        ans = -1
        for i in range(min(len(nums),k-1)):
            ans = max(ans,nums[i])
        if k < len(nums):
            ans = max(ans, nums[k])
            

        return ans
        