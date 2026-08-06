class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        seen = Counter(t)
        if s == t:
            return s
        if len(t) > len(s):
            return ""
        window = {}
        def valid():
            for ch in seen:
                if window.get(ch,0) < seen[ch]:
                    return False
            return True
        l = 0
        minv = float('inf')
        ans = ""
        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch,0)+1
            while valid():
                if r-l+1 < minv:
                    minv = r-l+1
                    ans = s[l:r+1]
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
        return ans



        