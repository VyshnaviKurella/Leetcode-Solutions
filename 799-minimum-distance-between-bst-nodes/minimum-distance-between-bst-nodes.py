# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    ans, prev = float('inf'), -1
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left: self.minDiffInBST(root.left)
        if self.prev != -1: self.ans = min(self.ans, root.val - self.prev)
        self.prev = root.val
        if root.right: self.minDiffInBST(root.right)
        return self.ans
        