import heapq
import sys
INF = int(1e9)

n, m, c = map(int,sys.stdin.readline().split()) #도시개수, 통로개수, 메시지보내는도시
graph = [[] for _ in range(n+1)] #노드와 간선 정보
distance = [INF] * (n+1) #최단거리 초기화 리스트
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append((y, z)) #x에서 y로 가는 데에 z걸림

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) #최단거리, 위치
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist: #이미 지나온 자리...
            continue
        for x in graph[now]: #x = (가는곳, 가는비용)
            cost = dist + x[1]
            if cost<distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(q, (cost, x[0]))

if __name__=="__main__":
    dijkstra(c)
    count = 0
    time = 0
    for d in distance:
        if d!=INF:
            count += 1
            time = max(time,d)
    
    print(count-1, time)
