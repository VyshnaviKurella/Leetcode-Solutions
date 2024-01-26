/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
    boolean res;
         if(p==null && q==null) 
		   res =true;			
         else if(p==null||q==null || p.val!=q.val) 
		    res = false;
        else
        {
         res = isSameTree(p.left,q.left) && isSameTree(p.right,q.right);
        }
	return res;  
    }
}