class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        n = len(customers)
        penalty = customers.count('Y')
        minv = penalty
        ans = 0
        for i in range(n):
            if customers[i] == 'Y':
                penalty -= 1
            else:
                penalty += 1
            if penalty < minv:
                minv = penalty
                ans = i+1
        return ans
            
