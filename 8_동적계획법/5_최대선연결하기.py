#최대 선 연결하기(LIS 응용)
import sys
n = int(sys.stdin.readline())
arr = [0] + list(map(int,sys.stdin.readline().split()))

dp = [0] * (n+1)
dp[1] = 1
for i in range(2,n+1):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))
