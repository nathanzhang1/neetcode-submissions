# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def checkBST(node, lt, gt):
            if node.val < lt and node.val > gt:
                left_valid, right_valid = True, True
                if node.left:
                    left_valid = checkBST(node.left, node.val, gt)
                if node.right:
                    right_valid = checkBST(node.right, lt, node.val)
                
                return left_valid and right_valid
            
            return False
        
        left_valid, right_valid = True, True
        if root.left:
            left_valid = checkBST(root.left, root.val, -math.inf)
        if root.right:
            right_valid = checkBST(root.right, math.inf, root.val)
        
        return left_valid and right_valid

        
# As we go down the tree we keep track of local upper and lower strict boundaries
# If root is leaf return true
# Check left, min=-inf, max=root.val
    # Recursively check left, min=-inf, max=left.val
    # Recursively check right, min=right.val, max=val