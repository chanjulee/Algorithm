import sys
from collections import deque

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        temp = queue.popleft()
        for i in graph[temp]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)
    visited = [False] * (N+1)
    bfs(graph, 1, visited)
    print(visited.count(True)-1)