'''
서로소 집합 자료구조: 합치지찾기(UnionFind)
-합집합: 두개의 원소가 포함된 집합을 하나의 집합으로 합치는 연사
-찾기: 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
서로소 집합은 무방향 그래프 내에서의 사이클을 판별
1) 각 간선을 확인하며 두 노드의 루트노드를 확인
-루트노드가 서로 다르면 합집합 수행
-루트노드가 같다면 사이클이 발생한 것임
2) 모든 간선에 대해 1번 과정 반복
'''

#특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    #루트노드를 찾을때까지 재귀적으로 호출
    if parent[x] != x: #루트 노드를 찾아 올라가는~
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b: #더 큰 루트노드가 더 작은 루트노드를 향하도록
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int,input().split()) #노드개수와 간선개수
parent = [0] * (v+1) #부모 테이블

edges = [] #간선 리스트
result = 0 #최종 비용

for i in range(1,v+1): #우선 부모는 자기자신
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int,input().split())
    edges.append((cost,a,b))
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b): #서로소 관계이면
        union_parent(parent, a, b) #합집합
        result += cost

print(result)