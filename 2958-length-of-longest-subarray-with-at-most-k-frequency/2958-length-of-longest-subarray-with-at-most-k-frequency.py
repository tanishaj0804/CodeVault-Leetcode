class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        seen = {}
        n = len(nums)
        i = j = 0
        res = 0
        while j<n:
            seen[nums[j]] = seen.get(nums[j],0)+1
            while seen[nums[j]] > k:
                seen[nums[i]] -= 1
                i += 1
            res = max(res,j-i+1)
            j += 1
        return res


        