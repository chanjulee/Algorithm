import sys
from collections import deque
queue = deque()

def bfs():
    while queue:
        h, x, y = queue.popleft()
        #d = [위,아래,왼,오,앞,뒤]
        dh = [1,-1,0,0,0,0]
        dx = [0,0,-1,1,0,0]
        dy = [0,0,0,0,-1,1]
        for i in range(6):
            tempH = h + dh[i]
            tempX = x + dx[i]
            tempY = y + dy[i]         
            if tempH<0 or tempH>=H or tempX<0 or tempX>=N or tempY<0 or tempY>=M:
                continue
            if graph[tempH][tempX][tempY]==0: #안익은 애 발견
                graph[tempH][tempX][tempY] = graph[h][x][y]+1 #걸린 시간 기록
                queue.append((tempH,tempX,tempY))

if __name__ == "__main__":
    M, N, H = map(int,sys.stdin.readline().split())
    graph = [[list(map(int,sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
    #print(graph) print(graph[1][1][2])
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if graph[h][i][j]==1:
                    queue.append((h,i,j))
    bfs()       
    flag = False
    graphMax = []
    for h in graph:
        graphMaxTemp = []
        for n in h:
            graphMaxTemp.append(max(n))
            if 0 in n: flag = True
        graphMax.append(max(graphMaxTemp))
    if flag:
        print(-1)
    else:
        print(max(graphMax)-1)