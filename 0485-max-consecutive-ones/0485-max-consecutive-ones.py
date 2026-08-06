class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxv = 0
        for num in nums:
            if num:
                count += 1
            else:
                count = 0
            maxv = max(maxv,count)
        return maxv
        