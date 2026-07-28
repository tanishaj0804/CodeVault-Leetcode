class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = curr = 0
        for i in range(len(nums)):
            prev,curr = curr, max(curr,prev+nums[i])
        return curr

        