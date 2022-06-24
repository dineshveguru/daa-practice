from numpy import minimum


inf = 9999999
v = int(input("enter number of vertices: "))
graph = []
for i in range(v):
    node = []
    for j in range(v):
        element = input(f"enter {i} - {j}th distance: ")
        if element.upper() == "INF":
            node.append(inf)
        else:
            node.append(int(element))
    graph.append(node)
selected = [0 for i in range(v)]
no_edge = 0
selected[0] = True
print("edge: weight\n")
while no_edge < v - 1:
    mininum = inf
    for i in range(v):
        if selected[i]:
            for j in range(v):
                if not selected[j] and graph[i][j]:
                    if mininum > graph[i][j]:
                        minimum = graph[i][j]
                        x = i
                        y = j
    print(str(x) + " - " + str(y) + " : " + str(graph[x][y]))
    selected[y] = True
    no_edge += 1
