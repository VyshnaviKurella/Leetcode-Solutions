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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode temp = new ListNode(0, head);
        ListNode leftpointer = temp, curr = head;
        ListNode prev = null; 
        for(int i=0; i<left-1; i++){
            leftpointer = curr;
            curr = curr.next;
        }      
        for(int i=0; i<right-left+1; i++){
            ListNode tmp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = tmp;
        }       
        leftpointer.next.next = curr;
        leftpointer.next = prev;
        return temp.next;
    }
}