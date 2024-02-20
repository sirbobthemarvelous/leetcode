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
    public ListNode middleNode(ListNode head) {
        ListNode speedy = head, slow = head;
        while(speedy != null && speedy.next != null){
            slow = slow.next;
            speedy = speedy.next.next;
        } 
        return slow;
    }
}