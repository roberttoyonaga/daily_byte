class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        '''
        Seems like you need to build a directed graph. 
        Each pair in prerequisites is an edge. 
        Courses in a cycle cannot be taken. The cycle does not have to be isolated, it just has to exist.
        Are there ANY cycles?
        
        Use DFS to find cycles
        '''
        #construct graph using adjacency lists
        graph = {i:[] for i in range(numCourses)}
        
        #populate graph
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        
        visited = set() #.clear()
        
        for course in graph: #try only from every possible starting point
            if not self.dfs(course, visited, graph): 
                return False
        return True
        
    def dfs(self,course, visited, graph):
        if course in visited:
            return False # cycle, cannot reach this course
        if len(graph[course]) == 0: #course has no prerequisites
            return True
    
        visited.add(course) 
        #if any of the prereqs are not reachable, then this course is also not reachable
        for prereq in graph[course]:
            if not self.dfs(prereq,visited,graph): 
                return False
        graph[course] = [] # memoization, don't redo work
        visited.remove(course) #reuse visited array
        return True
        
            