class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            res = []
            while i:
                res.append(i%2)
                i = i//2
            val = res.count(1)
            ans.append(val)
        return ans
            
            