class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res= []
        def backtrack(path,i,rem):
            if rem<0:
                return
            elif rem == 0:
                res.append(path[:])
            else:
                for j in range(i,len(candidates)):
                    if j>i and candidates[j] == candidates[j-1]:
                        continue
                    path.append(candidates[j])
                    backtrack(path,j+1,rem-candidates[j])
                    path.pop()
        backtrack([],0,target)
        return res
        