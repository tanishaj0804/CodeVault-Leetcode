"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        q = deque()
        q.append((root,1))
        while q:
            node,depth = q.popleft()
            if node.children:
                for nei in node.children:
                    q.append((nei,depth+1))
        return depth