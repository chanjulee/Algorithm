import sys
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))    
    while queue:
        x, y = queue.popleft()
        #d = [상,하,좌,우]
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range(4): #상하좌우 확인
            tempX = x + dx[i]
            tempY = y + dy[i]            
            if tempX<0 or tempX>=N or tempY<0 or tempY>=M:
                continue
            if graph[tempX][tempY]==0:
                continue
            if graph[tempX][tempY]==1:
                graph[tempX][tempY] = graph[x][y]+1 #거리기록
                queue.append((tempX,tempY))
    return graph[N-1][M-1]

if __name__ == "__main__":
    N, M = map(int,sys.stdin.readline().split())
    graph = []
    for x in range(N):
        x = sys.stdin.readline().rstrip()
        temp = []
        for y in x:
            temp.append(int(y))
        graph.append(temp)
    print(bfs(0,0))
