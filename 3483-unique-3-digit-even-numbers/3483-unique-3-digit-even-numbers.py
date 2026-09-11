class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        if all(num%2 == 1 for num in digits):
            return 0
        f = Counter(digits)
        res = 0
        for n in range(100,1000,2):
            i,r = divmod(n,100)
            j,k = divmod(r,10)
            res += f[i] > 0 and f[j] > (i==j) and f[k] > (i==k)+(j==k)
        return res
        
        