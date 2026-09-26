# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val : i for i, val in enumerate(inorder)}
        preorder_start = 0

        def dfs(left, right):
            nonlocal preorder_start

            if left > right:
                return None
            
            root = TreeNode()
            root.val = preorder[preorder_start]

            preorder_start += 1

            i = inorder_map[root.val]

            root.left = dfs(left, i - 1)
            root.right = dfs(i + 1, right)

            return root
        
        return dfs(0, len(preorder) - 1)