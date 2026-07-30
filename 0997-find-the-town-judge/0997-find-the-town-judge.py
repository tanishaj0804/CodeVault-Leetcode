class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        incoming = [0]*(n+1)  #n+1 because nodes are from 1 to N 
        outgoing = [0]*(n+1)
        for u,v in trust:
            incoming[v] += 1
            outgoing[u] += 1
        for judge in range(1,n+1):
            if incoming[judge] == n-1 and outgoing[judge] == 0:
                #the judge has all n-1 incoming to it and 0 outgoing from it
                return judge
        return -1
                
        