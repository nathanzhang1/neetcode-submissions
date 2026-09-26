class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        # DFS with pruning
        def dfs(r, c, node):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            
            ch = board[r][c]
            if ch == '#' or ch not in node.children:
                return

            next_node = node.children[ch]

            if next_node.word:
                result.append(next_node.word)
                next_node.word = None   # avoid duplicates

            # mark visited
            board[r][c] = '#'

            # explore neighbors
            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            # restore cell
            board[r][c] = ch

            # ---- TRIE PRUNING ----
            # If this path is no longer useful, delete it
            if not next_node.children and next_node.word is None:
                del node.children[ch]

        # Start DFS from valid starting letters only
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return result