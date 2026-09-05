class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res =[]
        n = len(s)
        def backtrack(i,curr,d):
            if i == n and d == 4:
                res.append(curr[:-1])
                return
            if i>= n or d == 4:
                return
            if s[i] == '0':
                backtrack(i+1,curr+'0.',d+1)
                return
            for j in range(1,4):
                p = s[i:i+j]
                if int(p) > 255:
                    break
                backtrack(i+j,curr+p+'.',d+1)
        backtrack(0,"",0)
        return  res

        