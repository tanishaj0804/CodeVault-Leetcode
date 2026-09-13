class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        #get the indices in img1 & img2 when the value is 1
        A = [(i,j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        B = [(i,j) for i in range(n) for j in range(n) if img2[i][j] == 1]
        cnt = [[0]*(2*n) for _ in range(2*n)]
        best = 0
        for ax, ay in A:
            for bx, by in B:
                # Required shift to move A's point onto B's point
                dx = bx-ax+n
                dy = by-ay+n
                cnt[dx][dy] += 1
                # Keep maximum overlap
                best = max(best,cnt[dx][dy])
        return best

    
        