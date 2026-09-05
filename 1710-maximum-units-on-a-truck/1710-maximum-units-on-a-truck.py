class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:-x[1])
        i = 0
        val = 0
        while truckSize > 0 and i < len(boxTypes):
            take = min(boxTypes[i][0],truckSize)
            val += take * boxTypes[i][1]
            truckSize -= take
            i += 1
        return val



        