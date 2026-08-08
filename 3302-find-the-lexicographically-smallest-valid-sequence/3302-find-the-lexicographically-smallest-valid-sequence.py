class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        m = len(word1)
        n = len(word2)
        match = [-1]*n
        i = m-1
        j = n-1
        while i>= 0  and  j>= 0:
            if word1[i] == word2[j]:
                match[j] = i
                j -= 1
            i -= 1

        res = []
        i=j=0
        changed = False
        while i<m and j<n:
            if word1[i] == word2[j]:
                res.append(i)
                j+=1
            elif not changed and (j==n-1 or match[j+1] > i):
                changed = True
                res.append(i)
                j += 1
            i += 1
        return res if j==n else [] 
