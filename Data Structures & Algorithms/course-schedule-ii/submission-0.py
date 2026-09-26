class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacencySets = {} # Prereq to class(es)
        inDegreeCount = {x : 0 for x in range(numCourses)} # Class to prereq count

        for p in prerequisites:
            if p[1] not in adjacencySets:
                adjacencySets[p[1]] = set()
            adjacencySets[p[1]].add(p[0])
            inDegreeCount[p[0]] += 1
        
        q = deque()

        for i in inDegreeCount:
            if inDegreeCount[i] == 0:
                q.append(i)
        
        if not q:
            return []

        output = []

        while q:
            n = q.popleft()
            output.append(n)
            if n in adjacencySets:
                for neighbor in adjacencySets[n]:
                    inDegreeCount[neighbor] -= 1
                    if inDegreeCount[neighbor] == 0:
                        q.append(neighbor)
        
        if len(output) != numCourses:
            return []

        return output