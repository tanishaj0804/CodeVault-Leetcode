class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        ans = []
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in seen:
                ans += [nums.index(diff),i]
            seen[nums[i]] = i
        return ans