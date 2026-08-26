class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq = Counter(p)
        res = []
        window = {}
        i = j = 0
        while j<len(s):
            window[s[j]] = window.get(s[j],0)+1
            while (j-i+1) > len(p):
                window[s[i]] -= 1
                if window[s[i]] == 0:
                    del window[s[i]]
                i += 1
            if window == freq:
                res.append(i)
            j += 1
        return res


            

        
        