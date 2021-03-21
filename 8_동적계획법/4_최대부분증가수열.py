#최대 부분 증가수열
import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
dp = [1] * n #[0]으로 초기화하면 틀림.. 왜?
for i in range(1, n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
