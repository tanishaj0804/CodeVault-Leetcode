class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        minv = [0]*n
        minv[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            minv[i] = min(nums[i], minv[i+1])
        maxv = nums[0]
        for i in range(n):
            maxv = max(maxv,nums[i])
            if maxv - minv[i] <= k:
                return i
        return -1