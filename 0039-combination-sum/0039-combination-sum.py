class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(path,i,rem):
            if rem<0:
                return
            if rem == 0:
                res.append(path[:])
            else:
                for j in range(i,len(candidates)):
                    path.append(candidates[j])
                    backtrack(path,j,rem-candidates[j])
                    path.pop()
        backtrack([],0,target)
        return res
