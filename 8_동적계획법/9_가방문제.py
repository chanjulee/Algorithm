#가방문제(냅색 알고리즘 : Knapsack algorithm)
import sys
n, m = map(int,sys.stdin.readline().split()) #보석종류, 무게제한
dp = [0] * (m+1) #dp[j]: 가방에 j무게까지 담았을때 보석의 최대가치

for i in range(n):
    w, v = map(int,sys.stdin.readline().split()) #보석무게, 보석가치
    for j in range(w, m+1):
        dp[j] = max(dp[j], dp[j-w]+v)

print(dp[-1])