# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_ancestors, q_ancestors = [], []

        def dfs(node, ancestors):
            nonlocal p_ancestors, q_ancestors
            
            if node.val == p.val:
                p_ancestors = ancestors.copy()
            if node.val == q.val:
                q_ancestors = ancestors.copy()
            
            if node.left:
                dfs(node.left, ancestors + [node.left])
            if node.right:
                dfs(node.right, ancestors + [node.right])
        
        dfs(root, [root])

        i, j = 0, 0
        LCA = p_ancestors[0]

        while i < len(p_ancestors) and j < len(q_ancestors):
            if p_ancestors[i].val != q_ancestors[j].val:
                break
            LCA = p_ancestors[i]
            i += 1
            j += 1

        return LCA