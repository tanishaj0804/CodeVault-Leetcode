class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 0:
            return 0
        curr = maxv = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                curr += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                curr = 1
            maxv = max(maxv,curr)
        return maxv
            




        