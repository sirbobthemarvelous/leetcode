class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      dummyNode = resList = ListNode(None)
      carryVar = 0
      while l1 or l2 :
          sum_val = carryVar
          if l1 != None:
              sum_val += l1.val
              l1 = l1.next
          if l2 != None:
              sum_val += l2.val
              l2 = l2.next
          carryVar = sum_val // 10
          resList.next = ListNode(sum_val % 10)
          resList = resList.next

      if carryVar == 1:
          resList.next = ListNode(carryVar)

      return dummyNode.next
"""