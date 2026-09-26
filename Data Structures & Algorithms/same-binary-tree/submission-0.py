# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                path_signature.append('N')
                return
            
            path_signature.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        path_signature = []
        dfs(p)
        p_path = path_signature.copy()

        path_signature = []
        dfs(q)
        q_path = path_signature.copy()

        return p_path == q_path