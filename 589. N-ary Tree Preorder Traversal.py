"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        arr = []
        def order(root):
            if root is None: return None
            arr.append(root.val)
            for i in root.children:
                order(i)    
        order(root)
        return arr
    """
    def deeper(self, root:'Node' ,workingList: List[int]) -> List[int]:
        if root.children is not None: workingList.append(deeper(root.children, workingList))
        return workingList
    def preorder(self, root: 'Node') -> List[int]:
        workingList = []
        deeper(root, workingList)
        return workingList """
    