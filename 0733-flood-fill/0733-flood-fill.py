class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        if image[sr][sc] ==color:
            return image
        def dfs(i,j):
            if i<0 or j<0 or i>=len(image) or j>=len(image[0]):
                return
            if image[i][j] != orig:
                return 
            image[i][j] = color
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        dfs(sr,sc)
        return image

        