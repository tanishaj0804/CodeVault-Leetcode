class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        def winner(i,j):
            if i == j:
                return nums[i]
            return max(
                nums[i] - winner(i+1,j),
                nums[j] - winner(i,j-1))
        return winner(0,n-1) >= 0