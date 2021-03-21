#가장 높은 탑 쌓기(LIS 응용)
import sys
n = int(sys.stdin.readline())

dp = []
tower = []
for _ in range(n):
    a, b, c = map(int,sys.stdin.readline().split())
    tower.append([a,b,c]) #넓이, 높이, 무게
towerSort = sorted(tower, key=lambda x:(x[0]), reverse=True) #넓이
for t in towerSort:
    dp.append(t[1])

for i in range(1,n):
    for j in range(i):
        if towerSort[i][2]<towerSort[j][2]:
            dp[i] = max(dp[i],dp[j]+towerSort[i][1])
#print(dp)
print(max(dp))