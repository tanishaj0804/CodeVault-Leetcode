class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for j in range(len(haystack)-len(needle)+1):
            i = 0
            while i < len(needle) and haystack[i+j] == needle[i]:
                i += 1
            if i == len(needle):
                return j
        return -1 
