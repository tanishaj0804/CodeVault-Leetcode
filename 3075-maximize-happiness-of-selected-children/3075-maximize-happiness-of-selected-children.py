class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse = True)
        happy = 0
        for i in range(k):
            happy += max(0,happiness[i]-i)
        return happy
        
        