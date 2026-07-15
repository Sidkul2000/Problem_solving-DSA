# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # l = self.maxDepth(root.left)
        # r = self.maxDepth(root.right)
        # return 1 + max(l,r)
        
        if not root:
            return 0
        queue = deque()
        depth = 0
        queue.append(root)
        while queue:
            level = len(queue)
            for i in range(level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth