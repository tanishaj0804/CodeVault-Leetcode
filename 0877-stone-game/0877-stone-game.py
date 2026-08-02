class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return True
        #since the piles array is of even length and sum of stones is always odd
        #Alice picks first and gets the chance to wither find odd indices sum or even indices sum and decide which one is greater
        #Alice always has odd parity and bob always had even parity(check solutions to understand this)
        #special case of predict the winner (486) with 2 additional constraints