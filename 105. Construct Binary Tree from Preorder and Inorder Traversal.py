# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        inorderMap = {}
        for i in range(len(inorder)):
            inorderMap[inorder[i]] = i
        def helper(l, r):
            if l > r:
                return None
            root = TreeNode(preorder.pop(0))
            mid = inorderMap[root.val]
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root
        root = helper(0, len(inorder) - 1)
        return root
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def INeedHelp(preStart: int, inStart: int, inEnd: int, preorder: List[int], inorder: List[int]) -> TreeNode:
        #checking to make sure it's not out of bounds
            if preStart > len(preorder) or inStart > inEnd:
                return None
            
        #obtain the root node with the current preorder element
            root = TreeNode(preorder[preStart])
        
        #declare the inorder's Index 
            inIndex = 0
        
        #find the preorder's element's index within the inorder
            for i in range(inStart, inEnd+1):
                if(inorder[i] == root.val):
                    inIndex=i
        
        #doing the left of the inIndex aka the end for the left subtree
            root.left = INeedHelp(preStart+1, inStart, inIndex-1, preorder, inorder)
        #prestart + length of the left subtree + 1 = right subtree i guess
            root.right = INeedHelp(preStart + inIndex - inStart +1, inIndex+1, inEnd, preorder, inorder)
        
        #checking the array indexes recursively
        #maybe i have to append the returns in a list?
        return INeedHelp(0,0, len(inorder)-1, preorder, inorder)
        """
    
        