# https://leetcode.com/problems/symmetric-tree/
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        if root is None:
            return True
        
        return self.Mirrowed(root.left, root.right)
        
    def Mirrowed(self, left, right):
        # Symetric case True
        if left is None and right is None:
            return True
        # They don't match so False
        if left is None or right is None:
            return False
        # Don't match so False and the other cases fullify first condition
        if left.val != right.val:
            return False
        
        return self.Mirrowed(left.left, right.right) and self.Mirrowed(left.right, right.left)
