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
    public boolean isBalanced(TreeNode root) {
   
    if(root==null)
        return true;
    
    if(height(root)!=-1)
     return  true;
    else
    return false;
    
}
public int height(TreeNode node){
    if(node==null)
        return 0;
    
    int leftHeight=height(node.left);
    if(leftHeight==-1){
        return -1;
    }
    int rightHeight=height(node.right);
    if(rightHeight==-1){
        return -1;
    }
    if(leftHeight-rightHeight<-1 || leftHeight-rightHeight>1){
        return -1;
    }
    return Math.max(leftHeight,rightHeight)+1;
}
}