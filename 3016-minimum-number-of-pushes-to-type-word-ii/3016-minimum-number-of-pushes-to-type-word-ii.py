class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        freq = Counter(word)
        ans = 0
        cost = 0
        for i,f in enumerate(sorted(freq.values(),reverse = True)):
            cost = (i//8)+1
            ans += cost*f
        return ans
        