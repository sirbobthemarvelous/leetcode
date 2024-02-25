# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #check length
        #stack push and pop
        # or just use FLoyd SOlution

        slow, fast, prev = head, head, None
        while fast and fast.next: 
            #slow get to middle while fast gets to end
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        # prev goes forward
        while slow: #reversal
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow: # check the reverse
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True
        
        