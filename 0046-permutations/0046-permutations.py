class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def permute(id):
            if id == len(nums):
                ans.append(nums[:])
                return
            for i in range(id, len(nums)):
                nums[id], nums[i] = nums[i], nums[id]
                permute(id+1)
                nums[id], nums[i] = nums[i], nums[id]

        permute(0)
        return ans

        