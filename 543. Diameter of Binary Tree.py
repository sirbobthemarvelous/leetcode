# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def height(node=root):
            if not node:
                return 0
            if not node.left and not node.right:
                return 0
            chord = le = ri = 0
            if node.left:
                le = height(node.left)
                chord += 1 + le
            if node.right:
                ri = height(node.right)
                chord += 1 + ri
            self.diameter = max(chord, self.diameter)
            return 1+max(le, ri)
        height()
        return self.diameter