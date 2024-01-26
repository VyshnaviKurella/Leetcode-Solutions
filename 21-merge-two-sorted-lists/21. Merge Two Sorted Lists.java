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
    // ListNode head = new ListNode();      
    //     if(list1 == null && list2 == null) 
    //       return null;  
    //     else
    //     { 
    //      if(list1 == null) 
    //       return list2;
    //      else if(list2 == null) 
    //       return list1;
    //     }
    //     if(list1.val > list2.val) 
    //     { 
    //         head = list2;
    //         list2 = list2.next;
    //     }
    //     else 
    //     {
    //         head = list1;
    //         list1 = list1.next;
    //     }  
    //     head.next = mergeTwoLists(list1,list2);
    //     return head;


    ArrayList<Integer> a = new ArrayList<>();
// a.add(0);
 while(list1!=null)
 {   a.add(list1.val);
        list1 = list1.next;
    }
    while(list2!=null)
    {
         a.add(list2.val);
        list2 = list2.next;
    }
    Collections.sort(a);
    // for(int i=0;i<a.size();i++)
    // {
    //     System.out.println(a.get(i));
    // }
    // int n = a.get(0);
  ListNode res = new ListNode();
  res=res.next;
 for(int i=a.size()-1;i>=0;i--)
    {
         res = new ListNode(a.get(i),res);
        //  res = res.next;    
    }
     
  return res;
//   return n;
    }
}