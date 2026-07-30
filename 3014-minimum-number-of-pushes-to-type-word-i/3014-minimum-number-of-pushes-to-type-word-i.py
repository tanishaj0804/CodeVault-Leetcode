class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        cost=0
        ans = 0
        freq = Counter(word)
        for i,f in enumerate(sorted(freq.values(),reverse=True)):
            cost = (i//8) + 1
            ans += cost*f
        return ans
        

        