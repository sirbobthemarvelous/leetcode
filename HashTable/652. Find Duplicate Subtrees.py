# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees ={}
        duplicates = []
        def serialize(n):
            if not n:
                return ''
            left = serialize(n.left)
            right = serialize(n.right)

            subtree = f'{n.val},{left},{right}'
            subtrees[subtree] = subtrees.get(subtree, 0) + 1

            if subtrees[subtree] == 2:
                duplicates.append(n)
            return subtree
        serialize(root)
        return duplicates      