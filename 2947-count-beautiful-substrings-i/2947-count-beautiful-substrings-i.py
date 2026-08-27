class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        v = "aeiou"
        count = 0
        for i in range(len(s)):
            vc = cc = 0
            for j in range(i,len(s)):
                if s[j] in v:
                    vc += 1
                else:
                    cc += 1
                if vc == cc and (vc*cc)%k == 0:
                    count += 1
        return count

        