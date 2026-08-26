class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        res = []
        cols = set()
        diag1 = set()
        diag2 = set()
        def solve(row):
            if row == n:
                temp = []
                for r in board:
                    temp.append("".join(r))
                res.append(temp)
                return
            for col in range(n):
                if col in cols or (row+col) in diag1 or (row-col) in diag2:
                    continue
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row+col)
                diag2.add(row-col)

                solve(row+1)
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row+col)
                diag2.remove(row-col)
        solve(0)
        return res


                

        