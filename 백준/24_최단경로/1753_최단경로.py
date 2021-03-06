import sys
import heapq
V, E = map(int,sys.stdin.readline().split())
k = int(sys.stdin.readline())
#노드의 연결 정보. u에서 v로 가는데 w걸리는 간선
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int,sys.stdin.readline().split())
    graph[u].append((v, w))
#최단거리 테이블
distance = [int(1e9)] * (V+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for x in graph[now]: # x = [어디로,얼마나]
            cost = dist + x[1]
            if cost<distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(q, (cost,x[0]))

if __name__=="__main__":
    dijkstra(k)
    for i in range(1, V+1):
        if distance[i]==int(1e9):
            print("INF")
        else:
            print(distance[i])