class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        def permute(id):
            if id == len(nums):
                ans.append(nums[:])
                return
            used = set()
            for i in range(id,len(nums)):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                nums[id], nums[i] = nums[i], nums[id]
                permute(id+1)
                nums[id], nums[i] = nums[i], nums[id]
        permute(0)
        return ans

        