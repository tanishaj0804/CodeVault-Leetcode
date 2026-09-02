class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        open = 0
        close = 0
        def backtrack(curr,open,close):
            if len(curr) == 2*n and open == n and close == n:
                res.append(curr)
                return
            if open < n:
                backtrack(curr + '(',open+1,close)
            if close < open:
                backtrack(curr + ')',open,close+1)
        backtrack("",0,0)
        return res
        