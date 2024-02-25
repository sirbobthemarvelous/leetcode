class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode curr = head;
        ListNode prev = null;
        ListNode start = null;
        while(curr!=null){
            n = n - 1;
            curr = curr.next;
            if(n<=0){
                if(start==null){
                    start = head;
                }
                else{
                    prev = start;
                    start = start.next;
                }
            }
        }
        if(prev==null){
            return start.next;
        }
        prev.next = start.next;
        return head;
    }
}