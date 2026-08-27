class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        cnt = s.count('1')
        if cnt < k:
            return ""
        i = j = 0
        ones = 0
        ans = ""
        while j < len(s):
            if s[j] == '1':
                ones += 1
            while ones == k:
                curr = s[i:j+1]
                if ans == "" or len(curr) < len(ans) or (len(curr) == len(ans) and curr < ans):
                    ans = curr
                if s[i] == '1':
                    ones -= 1
                i += 1
            j += 1
        return ans

        