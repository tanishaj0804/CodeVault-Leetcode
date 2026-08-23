class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        mid = len(num)//2
        left = num[:mid]
        right = num[mid:]
        if '?' not in num:
            return sum(map(int,left)) != sum(map(int,right))
        leftq = lefts = rightq = rights = 0
        for c in left:
            if c == '?':
                leftq += 1
            else:
                lefts += int(c)
        for c in right:
            if c == '?':
                rightq += 1
            else:
                rights += int(c)
        if (leftq + rightq)%2 == 1:
            return True
        diff = lefts - rights
        qdiff = rightq - leftq
        return diff*2 != 9*qdiff