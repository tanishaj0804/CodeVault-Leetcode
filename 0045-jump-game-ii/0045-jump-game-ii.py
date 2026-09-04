class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        jumps = 0
        vis = 0
        l = r = 0
        while r<len(nums)-1:
            for i in range(l,r+1):
                vis = max(vis,i+nums[i])
            l = r+1
            r = vis
            jumps += 1
        return jumps
        