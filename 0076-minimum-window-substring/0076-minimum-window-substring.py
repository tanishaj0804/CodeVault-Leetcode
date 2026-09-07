class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = Counter(t)
        window = {}
        if len(s) < len(t):
            return ""
        if s == t:
            return s
        i = j = 0
        minv = float('inf')
        ans = ""
        def isvalid():
            for ch in freq:
                if window.get(ch,0) < freq[ch]:
                    return False
            return True
        while j < len(s):
            ch = s[j]
            window[ch] = window.get(ch,0)+1
            while isvalid():
                if j-i+1 < minv:
                    minv = j-i+1
                    ans = s[i:j+1]
                window[s[i]] -= 1
                if window[s[i]] == 0:
                    del window[s[i]]
                i += 1
            j += 1
        return ans
        
            