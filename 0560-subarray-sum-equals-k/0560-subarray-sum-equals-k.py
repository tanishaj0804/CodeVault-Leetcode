class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        cnt = 0
        s = 0
        for num in nums:
            s += num
            if s-k in seen:
                cnt += seen[s-k]
            seen[s] = seen.get(s,0)+1
        return cnt