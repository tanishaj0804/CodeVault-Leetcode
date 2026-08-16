# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def getHeight(root):
            height = 0
            while root:
                height += 1
                root = root.left
            return height
        left = getHeight(root.left)
        right = getHeight(root.right)
        if left == right:
            return (2 ** left) + self.countNodes(root.right)
        else:
            return (2 ** right) + self.countNodes(root.left)
