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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
           if (root == null) 
             return result;
        boolean rToL = false;
        Queue<TreeNode> queue = new LinkedList<>();
           queue.add(root);       
        while (!queue.isEmpty()) 
        {
        int count = queue.size();
        List<Integer> level = new ArrayList<>();
         for (int i = 0; i < count; i++)
          {
          TreeNode node = queue.poll();
           if (rToL) 
            level.add(0, node.val);
            else 
            level.add(node.val);
        if (node.left != null) 
            queue.add(node.left);
        if (node.right != null)
            queue.add(node.right);
    }
    result.add(level);
    rToL = !rToL;
  }
      return result;
    }
}