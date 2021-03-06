'''
#힙-우선순위 큐를 구현하기 위한 자료구조 O(logN). 최소힙/최대힙
'''

'''import heapq
#오름차순 힙 정렬. 최소힙
def heapsort(iterable):
    h = []
    result = []
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value) #특정리스트에 데이터 넣을때
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h)) #특정리스트에 데이터 뺄때
    return result
result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

#내림차순 힙 정렬. 최대힙
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result
result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)'''

'''
현재 가장 가까운 노드를 힙에 저장
현재의 최단 거리가 가장 짧은 노드를 선택해야하므로 최소힙
'''
#다익스트라 알고리즘: 개선된 구현 방법
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) #10억(무한 의미)

#노드의 개수, 간선의 개수
n, m = map(int,input().split())
#시작 노드 번호
start = int(input())
#각 노드에 연결되어 있는 노드 정보 그래프
graph = [[] for i in range(n+1)]
#최단 거리 테이블 초기화
distance = [INF] * (n+1)
#모든 간선정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    #a번노드에서 b번노드로 가는 비용이 c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단경로는 0, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    #큐q가 비어있지 않다면
    while q:
        #가장 최단거리가 짧은노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now]<dist:
            continue
        #현재노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]#거리값
            #현재노드를 거쳐서 이동하는 거리가 더 짧은 경우
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
'''
노드의 개수 V. 최대 간선의 개수 E.
E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 매우 유사
O(ElogE) -> O(ElogV)
'''
#수행
dijkstra(start)

#모든 노드로 가기 위한 최단거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])