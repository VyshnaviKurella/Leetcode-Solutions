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
    public ListNode reverseList(ListNode head) {
        ListNode currentNode = head;
        ListNode prevNode = null;  
     
        while(currentNode != null) 
        { 
            ListNode tempNext = currentNode.next; 
            currentNode.next = prevNode;
            prevNode = currentNode;
            currentNode = tempNext;
        }
       return prevNode; 
    }
}