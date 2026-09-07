class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for st in strs:
            key = "".join(sorted(st))
            if key not in seen:
                seen[key] = []
            seen[key].append(st)
        return list(seen.values())            

        