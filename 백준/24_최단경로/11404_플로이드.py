import sys
if __name__=="__main__":
    n = int(sys.stdin.readline()) #도시개수
    m = int(sys.stdin.readline()) #버스개수
    INF = int(1e9)
    graph = [[INF]*n for _ in range(n)] #2차원 그래프
    for i in range(n):
        graph[i][i] = 0
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        if graph[a-1][b-1]>c: #노선이 여러개일수도 있다
            graph[a-1][b-1] = c

    #플로이드-워셜 알고리즘
    for k in range(n): #k는 거쳐가는 노드
        for a in range(n): #출발 노드
            for b in range(n):
                #a부터 b까지의 거리
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

    for x in graph:
        for y in x:
            if y==INF:
                print(0, end=" ")
            else:
                print(y, end=" ")
        print()