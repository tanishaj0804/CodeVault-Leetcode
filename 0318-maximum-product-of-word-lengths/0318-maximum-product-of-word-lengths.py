class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        n = len(words)
        sets = [set(word) for word in words]
        for i in range(n):
            for j in range(i+1,n):
                if sets[i] & sets[j] == set():
                    ans = max(ans, len(words[i])*len(words[j]))
        return ans
        