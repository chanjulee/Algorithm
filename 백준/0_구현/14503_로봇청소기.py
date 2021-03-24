import sys
n, m = map(int,sys.stdin.readline().split())
r, c, d = map(int,sys.stdin.readline().split())
status = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

def clean(x, y, d):
    status[x][y]=2 # 현재위치청소    
    dx = [-1,0,1,0] # 0-북 1-동 2-남 3-서 #왼쪽으로 회전할때마다 index+3
    dy = [0,1,0,-1]

    temp = [False]*4 # 네방향 상태저장
    tempD = d
    for i in range(4):
        tempD = (tempD+3)%4 # 0>3>2>1>0
        nx = x+dx[tempD]
        ny = y+dy[tempD]
        if nx<1 or ny<1 or nx>=n-1 or ny>=m-1: # 벗어나면 넘어가
            continue
        if status[nx][ny]==0: # 청소가능 발견
            return clean(nx,ny,tempD)
        elif status[nx][ny]==2: 
            temp[i] = True
    
    if temp[1]: #후진 가능
        tempD = (d+2)%4
        nx = x+dx[tempD]
        ny = y+dy[tempD]
        if nx<1 or ny<1 or nx>=n-1 or ny>=m-1: # 벗어나면 리턴
            return
        clean(nx,ny,d)
    else:
        return

clean(r,c,d)

result = 0
for x in status: 
    result += x.count(2)
print(result)
#print(status)