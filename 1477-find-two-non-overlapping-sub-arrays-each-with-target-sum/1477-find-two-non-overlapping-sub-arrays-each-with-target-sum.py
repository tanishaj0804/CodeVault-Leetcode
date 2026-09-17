class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        ans = len(arr)+1
        total = 0
        dp = [n]*(n+1)
        l = 0
        for r,x in enumerate(arr):
            total += x
            while total>target:
                total -= arr[l]
                l += 1
            dp[r+1] = dp[r]
            if total == target:
                ans = min(ans,r-l+1+dp[l])
                dp[r+1] = min(dp[r],r-l+1)
        return -1 if ans == n+1 else ans