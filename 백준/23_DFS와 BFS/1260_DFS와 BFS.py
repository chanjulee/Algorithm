import sys
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True # v 방문처리
    print(v, end = ' ')

    for i in graph[v]: # v랑 연결된 애들 방문처리
        if not visited[i]:
            dfs(graph, i, visited) # dfs는 재귀

def bfs(graph, v, visited):
    queue = deque([v]) # v 방문처리. bfs는 deque
    visited[v] = True

    while queue:
        temp = queue.popleft() # temp 빼면서
        print(temp, end = ' ')
        for i in graph[temp]: # temp 연결된 애들 방문처리
            if not visited[i]:
                queue.append(i)
                visited[i] = True

if __name__ == "__main__":
    N, M, V = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int,sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)
    for g in graph:
        g.sort()

    visited = [False] * (N+1)
    dfs(graph, V, visited)
    print()

    visited = [False] * (N+1)
    bfs(graph, V, visited)