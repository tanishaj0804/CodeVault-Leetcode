class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        incoming = defaultdict(int)
        outgoing = defaultdict(int)
        for u,v in paths:
            incoming[v] += 1
            outgoing[u] += 1
        for city in incoming:
            if outgoing[city] == 0:
                return city
        