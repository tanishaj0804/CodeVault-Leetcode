class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
        def subset(i):
            if i == len(s):
                res.append(curr[:])
                return
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if sub == sub[::-1]:
                    curr.append(sub)
                    subset(j+1)
                    curr.pop()
        subset(0)
        return res
            

        