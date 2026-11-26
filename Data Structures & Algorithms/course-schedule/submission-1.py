class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        prereqs = {}

        for i in range(numCourses):
            prereqs[i] = []
        
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
        
        visited = set()

        def foundCycle(c):
            # Found cycle
            if c in visited:
                return True
            
            # No more prereqs, this branch is safe
            if prereqs[c] == []:
                return False
            
            # More prereqs, add this course to visited path
            visited.add(c)

            # Search each prereq for cycle
            for p in prereqs[c]:
                if foundCycle(p):
                    return True
            
            # No cycle found down this branch, remove from path and clear prereq list
            visited.remove(c)
            prereqs[c] = []

            return False
        
        for i in range(numCourses):
            if foundCycle(i):
                return False
        
        return True
        
# Cannot finish all courses if we have a cycle in the prereq graph
# Prereq graph built using course -> prereqs
# Run recursive DFS on all courses, if any detects cycle return false
    # In each DFS track visited with set, if we travel to a visited course return false