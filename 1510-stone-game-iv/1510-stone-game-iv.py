class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def dfs(i):   # if i have i stones, can i win
            if i == 0:
                return False
            for j in range(1,isqrt(i)+1):
                if not dfs(i-j**2):  #currently at ith stone and u decide to remove j**2 stones
                    return True
            return False
        return dfs(n)
        