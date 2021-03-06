import sys
INF = int(1e9)
if __name__=="__main__":
    n, m = map(int,sys.stdin.readline().split()) #노드개수, 간선개수
    graph = [[INF]*n for _ in range(n)] #최단거리 초기화
    for i in range(n):
        graph[i][i] = 0 #자기자신으로 가는거리 0 초기화
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split()) #연결된 거리 1초기화
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = 1

    for k in range(n):
        for a in range(n):
            for b in range(n):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

    x, k = map(int, sys.stdin.readline().split()) #k를  거쳐 x로 가는
    distance = graph[0][k-1] + graph[k-1][x-1]
    #print(graph[0][k-1])
    #print(graph[k-1][x-1])
    #print(graph)
    if distance==INF:
        print("-1")
    else:
        print(distance)