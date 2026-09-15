class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def check(l,r):
            curr = s[l:r+1]
            return curr == curr[::-1]
        n = len(s)
        ans = 0
        start = 0
        for r in range(k-1,n):
            l = r-k+1
            if l>= start and check(l,r):
                ans += 1
                start = r+1
                continue
            l = r-k
            if l>=start and check(l,r):
                ans += 1
                start = r+1
        return ans