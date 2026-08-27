class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        n = len(s)
        i = j = 0
        maxv = 0
        while j<n:
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            maxv = max(maxv,j-i+1)
            j += 1
        return maxv
        