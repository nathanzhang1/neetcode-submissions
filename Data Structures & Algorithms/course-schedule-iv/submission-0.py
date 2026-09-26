class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        node_to_descendants = {}
        adjacency = {} # Prereq to class(es)

        for prereq, course in prerequisites:
            if prereq not in adjacency:
                adjacency[prereq] = set()
            adjacency[prereq].add(course)
                
        def dfs(n):
            if n not in node_to_descendants:
                node_to_descendants[n] = set()

                if n in adjacency:
                    for nei in adjacency[n]:
                        node_to_descendants[n] |= dfs(nei)

                node_to_descendants[n].add(n)
            return node_to_descendants[n]
        
        for i in range(numCourses):
            dfs(i)
        
        output = []
        for q in queries:
            if q[0] not in node_to_descendants:
                output.append(False)
            else:
                output.append(q[1] in node_to_descendants[q[0]])
        
        return output