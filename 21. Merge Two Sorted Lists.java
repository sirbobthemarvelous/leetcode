/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // easy situation
        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }
        // beginning
        ListNode beginning;
        // going through the nodes
        ListNode cursor;
        // figure out the beginning
        if (list1.val < list2.val) {
            cursor = beginning = new ListNode(list1.val);
            list1 = list1.next;
        } else {
            cursor = beginning = new ListNode(list2.val);
            list2 = list2.next;
        }
        // Loop until you hit the end of the list
        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                cursor.next = new ListNode(list1.val);
                list1 = list1.next;
            } else {
                cursor.next = new ListNode(list2.val);
                list2 = list2.next;
            }
            cursor = cursor.next;
        }
        // dump the remaining in list 1
        while (list1 != null) {
            cursor.next = new ListNode(list1.val);
            list1 = list1.next;
            cursor = cursor.next;
        }
        // dump the remaining in list 2
        while (list2 != null) {
            cursor.next = new ListNode(list2.val);
            list2 = list2.next;
            cursor = cursor.next;
        }
        return beginning;
    }
    
}