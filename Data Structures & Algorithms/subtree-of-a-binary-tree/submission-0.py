# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root1, root2):

            if not root1 and not root2:
                return True
            
            if root1 and root2 and root1.val == root2.val:
                return sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)
            
            return False
        
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if sameTree(node, subRoot):
                return True
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False