# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        #oh just switch around the direction of the next
 
        prev = None
        curr = head
        while(curr is not None):
            after = curr.next
            curr.next = prev # first one becomes the last one pointing to nothing
            # and later on you make it point backwards
            prev = curr # previous in this context means further along
            curr = after # and after follows
        head = prev

        return head
            
