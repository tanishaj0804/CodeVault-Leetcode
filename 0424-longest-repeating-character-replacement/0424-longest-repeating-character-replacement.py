class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        l = 0
        r = 0
        maxv = 0
        ans = 0
        while r<len(s):
            seen[s[r]] = seen.get(s[r],0)+1
            maxv = max(maxv,seen[s[r]])
            while (r-l+1) - maxv > k:
                seen[s[l]] -= 1
                l += 1
            ans = max(ans,r-l+1)
            r += 1
        return ans