INF = 9999999
G = [[0, 8, INF, 1],
     [INF, 0, 1, INF],
     [4, INF, 0, INF],
     [INF, 2, 9, 1]
     ]


def sol(g):
    distance = g
    n = len(g)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                distance[i][j] = min(
                    distance[i][j], distance[i][k] + distance[k][j])
    print(distance)


sol(G)
