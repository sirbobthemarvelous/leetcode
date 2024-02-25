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
    public ListNode swapPairs(ListNode head) {
        if(head == null) return null;
        if(head.next == null) return head;
        
        ListNode solution = new ListNode(0);
        solution.next = head;
        ListNode prev = solution;
        ListNode curr = head;
        ListNode after = head.next;
        
        while(curr!= null && after != null){
            //swap nodes
            prev.next = after; //after becomes head
            
            ListNode temporary = after.next; //store third node
            after.next = curr; //after points to curr
            prev = curr; //prev moves up before we edit curr
            curr.next = temporary; // curr points to third node
            curr = curr.next; // curr moves up
            if(temporary != null)
                after = temporary.next; //after moves up
        }
        return solution.next;
    }
}