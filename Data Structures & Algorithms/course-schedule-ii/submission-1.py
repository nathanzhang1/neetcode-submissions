class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        prereqs = {i: 0 for i in range(numCourses)}
        adj = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            prereqs[course] += 1
            adj[prereq].append(course)
        
        q = deque()
        for c in prereqs:
            if prereqs[c] == 0:
                q.append(c)
        
        order = []
        processed = 0
        while q:
            c = q.popleft()
            for i in adj[c]:
                prereqs[i] -= 1
                if prereqs[i] == 0:
                    q.append(i)
            order.append(c)
            processed += 1

        return order if processed == numCourses else []
        
# Kahn's algo
# Track course -> # prereqs, prereq -> course
# Put all courses with 0 prereqs into queue
# While queue not empty
    # Popleft a course from queue
    # For each of its adjacent courses
        # Decrement its # prereq count, append to queue if now 0
    # Add course to order list