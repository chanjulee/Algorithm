def function(n):
    dp = [None,1,1,1,2,2,3]
    if n in [1,2,3,4,5,6]:
        return dp[n]
    for i in range(7,n+1):
        temp = dp[i-1]+dp[i-5]
        dp.append(temp)
    return dp[n]

N = int(input())
for _ in range(N):
    n = int(input())
    print(function(n))