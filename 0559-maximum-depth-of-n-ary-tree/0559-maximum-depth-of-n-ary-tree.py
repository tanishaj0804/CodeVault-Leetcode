"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        maxd = 0
        stack = [(root,1)]
        while stack:
            node,depth = stack.pop()
            maxd = max(maxd,depth)
            for child in node.children:
                stack.append((child,depth+1))
        return maxd
        