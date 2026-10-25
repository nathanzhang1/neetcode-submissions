# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def find_diameter(node):
            if not node:
                return 

            nonlocal max_diameter

            def find_longest(node):
                if not node:
                    return 0

                left = 1 + find_longest(node.left)
                right = 1 + find_longest(node.right)

                return max(left, right)
        
            diameter = find_longest(node.left) + find_longest(node.right)

            max_diameter = max(diameter, max_diameter)

            find_diameter(node.left)
            find_diameter(node.right)
        
        find_diameter(root)

        return max_diameter

# Max diameter at node = longest from left + longest from right
# Longest from left = 1 + max(left child longest from left, left child longest from right)