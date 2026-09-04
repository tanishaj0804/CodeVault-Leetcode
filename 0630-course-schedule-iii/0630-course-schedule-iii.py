class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1])
        total = 0
        heap = []
        for d,l in courses:
            if l >= d:
                total += d
                heapq.heappush(heap,-d)
                
                if total > l:
                    longest = -heapq.heappop(heap)
                    total -= longest
        return len(heap)


        