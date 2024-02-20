# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        speedy = head
        slow = head
        while(speedy and speedy.next): #be sure that you're checking both current and next
            slow = slow.next
            speedy = speedy.next.next
        return slow
        """
        speedy = head
        slow = head
        onOff = 0
        while(speedy.next is not None):
            if(onOff%2==0): slow = slow.next
            speedy = speedy.next
            onOff+=1
        return slow
        """
        