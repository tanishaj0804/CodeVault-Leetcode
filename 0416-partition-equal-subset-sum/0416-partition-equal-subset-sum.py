class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumv = sum(nums)
        if sumv%2 == 0:
            target = sumv//2
        else:
            return False
        dp = [False]*(target+1)
        dp[0] = True
        for num in nums:
            for s in range(target-num,-1,-1):
                if dp[s]:
                    dp[s+num] = True
        return dp[target]
