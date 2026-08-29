# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node):
            if node is None:
                return [0,0]
            left = dfs(node.left)
            right = dfs(node.right)
            noRob = max(left[0],left[1]) + max(right[0],right[1])
            rob = node.val + left[0]+right[0]
            return [noRob,rob]
        dp =dfs(root)
        return max(dp[0],dp[1])
            