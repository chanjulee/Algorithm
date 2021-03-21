#네트워크 선 자르기(Top-Down : 재귀, 메모이제이션)
import sys
n = int(sys.stdin.readline())
dp = [0] * (n+1)

def dpTopDown(x):
    if x==0 or x==1 or x==2:
        return x
    if dp[x]!=0:
        return dp[x]
    dp[x] = dpTopDown(x-1) + dpTopDown(x-2)
    return dp[x]

print(dpTopDown(n))
