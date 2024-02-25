# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], min_val=float('-inf'), max_val=float('inf')) -> bool:
        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        left_valid = self.isValidBST(root.left, min_val , root.val)
        right_valid = self.isValidBST(root.right, root.val, max_val)

        return left_valid and right_valid

        
        """
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root or not root.left and not root.right: return True

        def kids(root, left, right) -> bool:
            valid = True
            if(left is not None):
                if(left.left is not None or left.right is not None):
                    valid = kids(left, left.left, left.right)
                if(left.val >= root.val): valid = False
            if(right is not None):
                if(right.left is not None or right.right is not None):
                    valid = kids(right, right.left, right.right)
                if (root.val >= right.val): valid= False
            return valid
        return kids(root,root.left,root.right) """