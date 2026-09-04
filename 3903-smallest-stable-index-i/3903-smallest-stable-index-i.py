class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if k == 0 and len(nums) == 1 and nums[0] == 0:
            return 0
        n  = len(nums)
        for i in range(n):
            maxv = max(nums[0:i+1])
            minv = min(nums[i:n])
            stable  = maxv-minv
            if stable <= k:
                return i
        return -1