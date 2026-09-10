# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        def PostOrder(root):
            if not root:
                return (0,0)
            left = PostOrder(root.left)   
            right = PostOrder(root.right)     
            nodeSum =  left[0] + right[0] + root.val
            nodecnt = left[1]+right[1]+1
            if root.val == (nodeSum//nodecnt):
                self.count += 1
            return (nodeSum,nodecnt)
        PostOrder(root)
        return self.count
        