class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(people)
        people.sort()
        l = 0
        r = n-1
        ans  = 0
        while l <= r:
            if people[l]+people[r] <= limit:
                l += 1
            ans += 1
            r -= 1
        return ans
        