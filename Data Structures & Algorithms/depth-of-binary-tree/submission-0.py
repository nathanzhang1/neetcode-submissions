# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque()
        q.append((root, 1))
        maxDepth = 1

        while q:
            node, cur_level = q.popleft()
            maxDepth = max(maxDepth, cur_level)
            if node.left:
                q.append((node.left, cur_level + 1))
            if node.right:
                q.append((node.right, cur_level + 1))
        
        return maxDepth