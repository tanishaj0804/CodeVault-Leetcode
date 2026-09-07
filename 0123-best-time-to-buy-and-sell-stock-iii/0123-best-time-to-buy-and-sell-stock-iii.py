class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        fbuy = sbuy = float('inf')
        fprofit = sprofit = 0
        for num in prices:
            fbuy = min(fbuy,num)
            fprofit = max(fprofit,num-fbuy)
            sbuy = min(sbuy,num-fprofit)
            sprofit = max(sprofit,num-sbuy)
        return sprofit
        