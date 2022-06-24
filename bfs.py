class Bfs:
    def __init__(self, n) -> None:
        self.graph = {}
        self.no_of_vertices = n
        self.vertices = set()
        self.visited = set()
        self.queue = []

    def addVertex(self, vertex):
        if vertex not in self.vertices:
            self.graph[vertex] = []
            self.vertices.add(vertex)
        else:
            print("this vertex already present in graph")

    def addEdge(self, node_one, node_two):
        if node_one not in self.vertices and node_two not in self.vertices:
            print("one of the vertices dont present in graph")
        else:
            self.graph[node_one].append(node_two)

    def solution(self, start):
        if start not in self.visited:
            self.visited.add(start)
            print(start)
            for i in self.graph[start]:
                self.queue.append(i)
            element = self.queue.pop(0)
            self.solution(element)

    def print_graph(self):
        print(self.graph)


graph = Bfs(5)
graph.addVertex(5)
graph.addVertex(7)
graph.addVertex(8)
graph.addVertex(4)
graph.addVertex(3)
graph.addVertex(2)
graph.addEdge(5, 3)
graph.addEdge(5, 7)
graph.addEdge(3, 4)
graph.addEdge(3, 2)
graph.addEdge(4, 8)
graph.addEdge(7, 8)


graph.print_graph()

graph.solution(5)
