class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        adjacencySets = {} # Prereq to class
        inDegreeCount = {x : 0 for x in range(numCourses)} # Class to no. prereqs

        for p in prerequisites:
            if p[1] not in adjacencySets:
                adjacencySets[p[1]] = set()
            adjacencySets[p[1]].add(p[0])

            if p[0] not in inDegreeCount:
                inDegreeCount[p[0]] = 0
            inDegreeCount[p[0]] += 1
        
        noInDegreeQueue = deque()
        
        for i in inDegreeCount:
            if inDegreeCount[i] == 0:
                noInDegreeQueue.append(i)
                
        if not noInDegreeQueue:
            return False
        
        processed = 0
        while noInDegreeQueue:
            n = noInDegreeQueue.popleft()
            processed += 1
            if n in adjacencySets:
                for neighbor in adjacencySets[n]:
                    inDegreeCount[neighbor] -= 1
                    if inDegreeCount[neighbor] == 0:
                        noInDegreeQueue.append(neighbor)
        
        return numCourses == processed