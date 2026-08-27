class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(target[i]) - ord('a')] -= 1
        t = list(target)
        def minString(count):
            res = []
            for i in range(26):
                res.append(chr(ord('a')+i)*count[i])
            return "".join(res)
        for i in range(len(t)-1,-1,-1):
            b = ord(t[i])-ord('a')
            count[b] += 1
            if min(count) < 0:
                continue
            for j in range(b+1,26):
                if count[j] > 0:
                    count[j] -= 1
                    t[i] = chr(ord('a')+j)
                    return "".join(t[:i+1]) + minString(count)
        return ""
    
        
            

