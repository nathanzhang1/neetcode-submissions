# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -100000

        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            path_sum = left + right + node.val

            max_sum = max(max_sum, path_sum)

            return node.val + max(left, right)
        
        dfs(root)
        
        return max_sum