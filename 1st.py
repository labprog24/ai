from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def bfs(self, vertex):
        visited = [False]*(max(self.graph)+1)
        queue = []
        queue.append(vertex)
        visited[vertex] = True
        while queue:
            m = queue.pop(0)
            print(m, end=' ')
            for neighbour in self.graph[m]:
                if visited[neighbour] == False:
                    queue.append(neighbour)
                    visited[neighbour] = True


g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

g.bfs(1)
