/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        // ListNode l1 = headA;
        ListNode l2 = headB;
        // ListNode res = new ListNode();
        // if(l1==l2)
        // return l1;
        while(headA!=null)
        {  while(l2!=null)          
           {   
               if(headA==l2)
                {    return headA;   }
                l2=l2.next;
           }
           headA=headA.next;
           l2=headB;
        }
     return null;   
    }
}