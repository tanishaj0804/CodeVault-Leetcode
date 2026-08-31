class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        seen = {0:1}
        s = 0
        for num in nums:
            s += num
            if s-k in seen:
                count += seen[s-k]
            seen[s] = seen.get(s,0) +1
        return count       