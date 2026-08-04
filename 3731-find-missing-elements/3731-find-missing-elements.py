class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res =[]
        nums.sort()
        curr = nums[0]
        for i in range(1,len(nums)):
            while nums[i] != curr+1:
                curr += 1
                res.append(curr)
            curr = nums[i]
        return res

        