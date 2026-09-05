class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for n,i,j in trips:
            events.append([i,n])
            events.append([j,-n])
        events.sort()
        for i,v in events:
            capacity -= v
            if capacity<0:
                return False
        return True