class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        freq = Counter(t)
        window = {}
        if s == t:
            return t
        if len(s) < len(t):
            return ""
        def valid():
            for ch in freq:
                if window.get(ch,0) < freq[ch]:
                    return False
            return True
        l = 0
        r = 0
        minv = float('inf')
        ans = ""
        while r < len(s):
            ch = s[r]
            window[ch] = window.get(ch,0) + 1
            while valid():
                if r-l+1 < minv:
                    minv = r-l+1
                    ans = s[l:r+1]
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            r += 1
        return ans


        