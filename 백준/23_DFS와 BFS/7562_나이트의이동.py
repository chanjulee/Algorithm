import sys
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        dx = [-1,-2,-2,-1,1,2,2,1]
        dy = [-2,-1,1,2,2,1,-1,-2]
        for i in range(8):
            tx = x+dx[i]
            ty = y+dy[i]
            if tx<0 or tx>=N or ty<0 or ty>=N: continue
            if graph[tx][ty]==0:
                graph[tx][ty] = graph[x][y]+1
                queue.append((tx,ty)) #appendleft써놔서 뻘짓함...
    return graph[gx][gy]

if __name__=="__main__":
    T = int(sys.stdin.readline())
    for i in range(T):
        N = int(sys.stdin.readline())
        graph = [[0]*N for _ in range(N)]
        x, y = map(int,sys.stdin.readline().split())
        gx, gy = map(int,sys.stdin.readline().split())
        if x==gx and y==gy:
            print(0)
            continue
        print(bfs(x,y))