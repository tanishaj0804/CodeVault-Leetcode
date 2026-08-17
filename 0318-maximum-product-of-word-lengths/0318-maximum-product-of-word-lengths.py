class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        masks = {}
        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            masks[mask] = max(masks.get(mask,0),len(word))
        key = list(masks)
        n = len(key)
        for i in range(n):
            for j in range(i+1,n):
                if key[i] & key[j] == 0:
                    ans = max(ans, masks[key[i]] * masks[key[j]])
        return ans
        