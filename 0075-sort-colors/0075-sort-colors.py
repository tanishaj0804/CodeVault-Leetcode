class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            swapped = False
            for j in range(0,n-1-i):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    swapped = True
        return nums