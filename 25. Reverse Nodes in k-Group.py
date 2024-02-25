# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        a = b = head
        for _ in range(k):
            if not b:
                return a
            b = b.next
            
        new_head = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return new_head
    
    def reverse(self, a, b):
        pre = None
        cur = a
        nxt = a
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
            
        return pre
        