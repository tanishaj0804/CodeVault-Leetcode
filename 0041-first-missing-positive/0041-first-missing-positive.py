class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [x for x in nums if x>0]
        nums = set(nums)
        n = len(nums)
        for i in range(1,n+2):
            if i not in nums:
                return i