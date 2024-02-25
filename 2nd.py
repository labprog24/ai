from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def dfs(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end= ' ')
        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)

    
    def dfsUtil(self, vertex):
        visited = set()
        self.dfs(vertex, visited)

    
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(2,0)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(4,5)
g.addEdge(3,6)

g.dfsUtil(2)
