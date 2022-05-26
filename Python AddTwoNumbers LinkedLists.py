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