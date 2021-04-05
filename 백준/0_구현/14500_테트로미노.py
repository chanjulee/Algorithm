import sys
n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

result = 0
def tetromino(x, y):
    global result
    dp = [0]*10
    dx = [0,0,0,0,1,1,1,2,2,3]
    dy = [0,1,2,3,0,1,2,0,1,0]
    for i in range(10):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m: continue
        dp[i] = graph[nx][ny]

    if dp[1]!=0:
        if dp[2]!=0:
            for x in [dp[3],dp[5],dp[6]]:
                if x!=0:
                    temp = dp[0]+dp[1]+dp[2]+x
                    result = max(result,temp)
        if dp[5]!=0:
            for x in [dp[6],dp[8]]:
                if x!=0:
                    temp = dp[0]+dp[1]+dp[5]+x
                    result = max(result,temp)
        if dp[4]!=0 and dp[5]!=0:
            temp = dp[0]+dp[1]+dp[4]+dp[5]
            result = max(result,temp)

    if dp[4]!=0:
        if dp[5]!=0:
            for x in [dp[6],dp[8]]:
                if x!=0:
                    temp = dp[0]+dp[4]+dp[5]+x
                    result = max(result,temp)
        if dp[7]!=0:
            for x in [dp[5],dp[8],dp[9]]:
                if x!=0:
                    temp = dp[0]+dp[4]+dp[7]+x
                    result = max(result,temp)

for i in range(n):
    for j in range(m):
        tetromino(i, j)

print(result)