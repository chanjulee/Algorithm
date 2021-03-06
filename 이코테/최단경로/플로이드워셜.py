'''
플로이드 워셜(Floyd-Warshall)
모든 노드에서 다른 모든 노드까지의 최단 경로를 계산.
다익스트라와 마찬가디로 단계별로 거쳐가는 노드를 기준으로 알고리즘 수행
but, 방문하지 않은 노드 중에 최단거리를 갖는 노드를 찾는과정X
2차원 테이블에 최단거리정보저장. 다이나믹 프로그래밍
구현은 쉽지만, 노드의 개수가 적어야 효율적... O(N^3)
'''
INF = int(1e9) #10억(무한)

#노드의 개수 및 간선의 개수
n = int(input())
m = int(input())
#2차원 리스트(그래프)를 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

#각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    #a에서 b로 가는 비용은 c라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

#점화식에 따라 플로이즈 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

#수행된 결과
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b]==INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
print()  