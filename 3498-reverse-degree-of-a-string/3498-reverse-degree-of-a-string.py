class Solution:
    def reverseDegree(self, s: str) -> int:
        sum = 0
        for i in range(len(s)):
            val = ord(s[i])-ord('a')
            sum += (i+1)*(26-val)
        return sum
        