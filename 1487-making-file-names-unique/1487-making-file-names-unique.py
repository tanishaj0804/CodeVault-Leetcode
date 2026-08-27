class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        seen = {}
        ans = []
        for file in names:
            if file not in seen:
                ans.append(file)
                seen[file] = 1
            else:
                k = seen[file]
                while file + '(' + str(k) + ')' in seen:
                    k += 1
                neww = file + '(' +str(k) + ')' 
                ans.append(neww)
                seen[file] = k+1
                seen[neww] = 1
        return ans
                
        