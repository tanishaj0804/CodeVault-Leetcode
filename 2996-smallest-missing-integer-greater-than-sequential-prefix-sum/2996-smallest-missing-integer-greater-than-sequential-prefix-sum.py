class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = nums[0]
        index = 0
        maxval = float("inf")
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                sum += nums[i+1]
                index = i+1
            else:
                break
        while sum < maxval:
            if sum not in nums:
                return sum
            sum += 1
        