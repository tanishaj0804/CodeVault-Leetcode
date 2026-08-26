class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = Counter(s1)
        for i in range(len(s2)-len(s1)+1):
            curr = s2[i:i+len(s1)]
            comp = Counter(curr)
            if comp == freq:
                return True
        return False
            

        