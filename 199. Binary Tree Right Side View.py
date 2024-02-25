# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=deque([root])
        if root==None:
            return []
        h=[]
        while(len(q)):
            n=len(q)
            h.append(q[-1].val)
            for i in range(n):
                k=q.popleft()
                if k.left:
                    q.append(k.left)
                if k.right:
                    q.append(k.right)
        return h