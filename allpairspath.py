from math import inf


# floyd warshall algorithm
while True:
    n, m, q = map(int, input().split(" "))
    if n == m == q == 0:
        break
    weights = [[inf if i != j else 0 for i in range(n)] for j in range(n)]
    for i in range(m):
        
        src, dest, weight = map(int, input().split(" "))
        weights[src][dest] = min(weights[src][dest], weight)
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                weights[i][j] = min(weights[i][j], weights[i][k] + weights[k][j])
    # Searching for negative cycles
    # Src: https://stackoverflow.com/questions/15709277/floyd-warshall-with-negative-cycles-how-do-i-find-all-undefined-paths
    # Comment author: https://stackoverflow.com/users/2205133/mseln
    for i in range(n):
        for j in range(n):
            if weights[i][j] != -inf:
                for k in range(n):
                    if weights[k][k] < 0 and weights[i][k] != inf and weights[k][j] != inf:
                        weights[i][j] = -inf
    for i in range(q):
        src, dest = map(int, input().split(" "))
        if weights[src][dest] == -inf:
            print("-Infinity")
        
        elif weights[src][dest] == inf:
            print("Impossible")
        else:
            print(weights[src][dest])
    print()