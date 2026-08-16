class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []
        cnt = {}
        ans = []
        for i in range(n-9):
            dna = s[i:i+10]
            cnt[dna] = cnt.get(dna,0)+1
            if cnt[dna] == 2:
                ans.append(dna) 
        return ans
        
        