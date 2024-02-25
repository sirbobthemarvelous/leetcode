# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        list3 = ListNode(100)
        original = list3
        while(list1 is not None or list2 is not None):
            list3.next = ListNode(0)
            list3 = list3.next
            if(list1 is None): 
                list3.val = list2.val
                list2 = list2.next
            elif(list2 is None):
                list3.val = list1.val
                list1 = list1.next
            else:
                if(list1.val <= list2.val):
                    list3.val = list1.val
                    list1 = list1.next
                else:
                    list3.val = list2.val
                    list2 = list2.next
        return original.next

        #leng = len(list1) + len(list2)
        #for x in range(leng):
