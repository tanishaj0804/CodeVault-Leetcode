class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        out = []
        for i in intervals:
            if not out or out[-1][-1] < i[0]:
                out.append(i)
            else:
                out[-1][-1] = max(out[-1][-1],i[-1])
        return out
        
        