class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:(x[0]-x[1]))
        N = len(costs)
        n= N//2
        cityA = []
        cityB = []
        for i,j in costs:
            if len(cityA)<n:
                cityA.append(i)
            else:
                cityB.append(j)
        return sum(cityA) + sum(cityB)
