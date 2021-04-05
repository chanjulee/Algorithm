import sys
n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

result = 0
def tetromino1(x, y, cnt, temp):
    global result
    if cnt == 4:
        result = max(result, temp)
        return
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m or visited[nx][ny]==1: continue #visited빼먹으면 틀림
        visited[nx][ny] = 1
        tetromino1(nx, ny, cnt+1, temp+graph[nx][ny])
        visited[nx][ny] = 0

def tetromino2(x, y):
    global result
    dv = [0] * 12
    dx = [-2,-1,-1,-1,0,0,0,0,1,1,1,2]
    dy = [0,-1,0,1,-2,-1,1,2,-1,0,1,0]
    for i in range(12):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m: continue
        dv[i] = graph[nx][ny]
    if dv[0]!=0 and dv[2]!=0:
        for z in [dv[1],dv[3]]:
            if z!=0:
                temp = graph[x][y]+dv[0]+dv[2]+z
                result = max(result,temp)
    if dv[4]!=0 and dv[5]!=0:
        for z in [dv[1],dv[8]]:
            if z!=0:
                temp = graph[x][y]+dv[4]+dv[5]+z
                result = max(result,temp)
    if dv[9]!=0 and dv[11]!=0:
        for z in [dv[8],dv[10]]:
            if z!=0:
                temp = graph[x][y]+dv[9]+dv[11]+z
                result = max(result,temp)
    if dv[6]!=0 and dv[7]!=0:
        for z in [dv[3],dv[10]]:
            if z!=0:
                temp = graph[x][y]+dv[6]+dv[7]+z
                result = max(result,temp)

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        tetromino1(i, j, 1, graph[i][j])
        visited[i][j] = 0
        tetromino2(i, j)

print(result)