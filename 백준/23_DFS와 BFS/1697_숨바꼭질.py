import sys
from collections import deque

def bfs(visited,v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        for i in range(3):
            if i==0: tempV = v-1
            elif i==1: tempV = v+1
            else: tempV = v*2
            if tempV<0 or tempV>100000: continue
            if visited[tempV]==0:
                visited[tempV]=visited[v]+1
                queue.append(tempV)
    return visited[K]

if __name__=="__main__":
    N, K = map(int,sys.stdin.readline().split())
    if N==K: #질문하기 봄...
        print(0)
        sys.exit()
    visited = [0] * 100001
    print(bfs(visited,N))