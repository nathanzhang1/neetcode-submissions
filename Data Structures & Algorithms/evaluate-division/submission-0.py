class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjacency = {}
        
        for i, eq in enumerate(equations):
            num, denom = eq
            val = values[i]

            if num not in adjacency:
                adjacency[num] = set()
            adjacency[num].add((denom, val))

            if denom not in adjacency:
                adjacency[denom] = set()
            adjacency[denom].add((num, 1/val))
                
        output = []
        visited = set()

        def dfs(cur_prod, cur_val, denom):
            visited.add(cur_val)
            if cur_val == denom:
                output.append(cur_prod)
                visited.remove(cur_val)
                return True
            
            for nei_val, nei_weight in adjacency[cur_val]:
                if nei_val not in visited and dfs(cur_prod * nei_weight, nei_val, denom):
                    visited.remove(cur_val)
                    return True
            
            visited.remove(cur_val)
            return False
        
        for num, denom in queries:
            if num not in adjacency or not dfs(1, num, denom):
                output.append(-1.0)
        
        return output