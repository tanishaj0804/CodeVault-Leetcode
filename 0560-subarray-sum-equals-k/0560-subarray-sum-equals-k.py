class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        count = 0
        s = 0
        for num in nums:
            s += num
            if s-k in seen:
                count += seen[s-k]
            seen[s] = seen.get(s,0)+1
        return count