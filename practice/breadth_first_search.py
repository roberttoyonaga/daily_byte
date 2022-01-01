from collections import defaultdict
from collections import deque
 
# This class represents a directed graph
# using adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self, start_node):
        visited = [False] * len(self.graph)#usefull init technique
        queue = deque([]) #popleft is O(1)

        queue.append(start_node)
        visited[start_node] = True

        while queue: #checks size not 0 
            s = queue.popleft()
            print(s," ")
            
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.BFS(2)
 