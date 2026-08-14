class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        seen = {}
        i = j = 0
        n = len(s)
        maxval = 0
        while j < n:
            seen[s[j]] = seen.get(s[j],0)+1
            while seen[s[j]] > 2:
                seen[s[i]] -= 1
                i += 1
            maxval = max(maxval,j-i+1)
            j += 1
        return maxval

        