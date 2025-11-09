# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getVal(root, value):
            if not root:
                return
            if not root.left and not root.right:
                value.append(root.val)
            getVal(root.left, value)
            getVal(root.right, value)

        val1 = []
        val2 = []

        getVal(root1, val1)
        getVal(root2, val2)

        return val1 == val2




        