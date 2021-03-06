'''다익스트라 최단 경로 알고리즘
특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산
음의 간선이 없을때 정상적으로 동작(현실 세계)
그리디, dp - 매 상황에서 가장 비용이 적은 노드 선택하는 과정 반복
동작 과정 - 
1) 출발 노드 설정
2) 최단 거리 테이블 초기화 (무한으로 설정, 자기자신은 0)
3) 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택 (탐욕적)
4) 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단거리 테이블 갱신
5) 3과 4를 반복
6) 마지막 노드는 안해도되는..최단거리값이 바뀌지않음
특징 - 
그리디알고리즘: 매상황에서 방문하지않은 가장비용이적은노드선택
한번처리된노드의 최단거리는 고정: 한단계당 하나의노드에대한 최단거리확정
테이블에 각 노드까지의 최단거리정보저장
'''
#다익스트라 간단구현: 매단계마다 1차원 테이블 모든원소확인(순차탐색)
import sys
input = sys.stdin.readline
INF = int(1e9) #10억(무한 의미)

#노드의 개수, 간선의 개수
n, m = map(int,input().split())
#시작 노드 번호
start = int(input())
#각 노드에 연결되어 있는 노드 정보 그래프
graph = [[] for i in range(n+1)]
#방문정보 담는 리느스
visited = [False] * (n+1)
#최단 거리 테이블 초기화
distance = [INF] * (n+1)

#모든 간선정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    #a번노드에서 b번노드로 가는 비용이 c
    graph[a].append((b, c))

#방문하디 않은 노드 중에서 가장 최단거리가 짧은노드번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i]<min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    #출발노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    #출발노드로부터 다른노드까지거리 갱신
    for j in graph[start]:
        distance[j[0]] = j[1]
    #시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        #현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] = True
        #현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧으면
            if cost<distance[j[0]]:
                distance[j[0]] = cost

#수행
dijkstra(start)

#모든 노드로 가기 위한 최단거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])