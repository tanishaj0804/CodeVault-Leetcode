class Solution:
    def countCommas(self, n: int) -> int:
        cnt = 0
        if n < 1000:
            return cnt
        for i in range(1000,n+1):
            cnt += 1
        return cnt
        