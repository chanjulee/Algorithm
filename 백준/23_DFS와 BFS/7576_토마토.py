import sys
from collections import deque
queue = deque()

def bfs():
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
            if graph[tempX][tempY]==0: #안익은 애 발견
                graph[tempX][tempY] = graph[x][y]+1 #걸린 시간 기록
                queue.append((tempX,tempY))

if __name__ == "__main__":
    M, N = map(int,sys.stdin.readline().split())
    graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j]==1:
                queue.append((i,j)) #익은 애들 넣어줌 #검색함...
    bfs()       
    flag = False
    graphMax = []
    for x in graph:
        graphMax.append(max(x))
        if 0 in x: flag = True
    if flag:
        print(-1)
    else:
        print(max(graphMax)-1)