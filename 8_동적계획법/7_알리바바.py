#알리바바와 40인의 도둑(Bottom-Up)
import sys
n = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

temp = 0
for i in range(n):
    dp[0][i] = graph[0][i] + temp
    temp = dp[0][i]
temp = 0
for j in range(n):
    dp[j][0] = graph[j][0] + temp
    temp = dp[j][0]

for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + graph[i][j]

print(dp[-1][-1])