# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if targetSum == root.val and not root.left and not root.right:
            return True
        
        if root.left:
            valid = self.hasPathSum(root.left, targetSum - root.val)
            if valid:
                return True
        
        if root.right:
            return self.hasPathSum(root.right, targetSum - root.val)
        
        return False