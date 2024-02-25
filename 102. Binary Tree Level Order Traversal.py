# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        def bfs(curr = root, level = 0):
            nonlocal arr
            if curr:
                if len(arr) > level:
                    arr[level].append(curr.val)
                else:
                    arr.append([curr.val])
                bfs(curr.left, level + 1)
                bfs(curr.right, level + 1)
            return
        bfs()
        return arr
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root.left is None and root.right is None: return root
        arr = []
        level = []
        level.append(root.val)
        arr.append(level)
        #oh just create an array of nodes to keep track of each level
        while(level is not None):
            level = []


        def addKids(self, root: Optional[TreeNode]) -> List[List[int]]:
            addKids(root.left)
            addKids(root.right)
            return  """