class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if sum(people) <= limit:
            return 1
        cnt = 0
        l = 0
        r = len(people)-1
        people.sort()
        while l<=r:
            if people[l] + people[r] <= limit:
                l += 1
            cnt += 1
            r -= 1  
        return cnt              
