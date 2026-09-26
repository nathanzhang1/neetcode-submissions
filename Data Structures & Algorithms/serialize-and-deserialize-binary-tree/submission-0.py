# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        output = []

        def recSerialize(node):
            nonlocal output
            if not node:
                output.append('N')
                return
            
            output.append(str(node.val))

            recSerialize(node.left)
            recSerialize(node.right)
        
        recSerialize(root)

        return " ".join(output)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data_list = data.split()
        cur = 0

        def recDeserialize():
            nonlocal cur
            if data_list[cur] == 'N':
                cur += 1
                return None
            
            root = TreeNode()
            root.val = data_list[int(cur)]

            cur += 1
            root.left = recDeserialize()
            root.right = recDeserialize()

            return root
        
        root = recDeserialize()
        
        return root