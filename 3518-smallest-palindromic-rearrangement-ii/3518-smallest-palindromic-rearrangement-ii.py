from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)
        halfway = [0]*26
        middle =""
        left =[]
        total = 0
        for ch in sorted(freq):
            idx = ord(ch)-ord('a')
            halfway[idx] = freq[ch]//2
            total += halfway[idx]
            if freq[ch]%2:
                middle = ch
        
        def Countw():
            t = total
            ways = 1
            for i in halfway:
                if i:
                    ways *= comb(t,i)
                    t -= i
                    if ways >= k:
                        return k
            return ways
        
        if Countw() < k:
            return ""
        
        left = []
        while total:
            for i in range(26):
                if halfway[i] == 0:
                    continue
                halfway[i] -= 1
                total -= 1

                ways = Countw()
                if ways >= k:
                    left.append(chr(i+ord('a')))
                    break
                else:
                    k-=ways
                    halfway[i] += 1
                    total += 1
        left = "".join(left)
        return left+middle+left[::-1]




