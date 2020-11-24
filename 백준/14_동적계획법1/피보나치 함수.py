def fibonacci(n):
    dp = [[1,0],[0,1],[1,1]]
    if n==0:
        return dp[0]
    elif n==1:
        return dp[1]
    elif n==2:
        return dp[2]
    for i in range(3,n+1):
        temp0=dp[i-1][0]+dp[i-2][0]
        temp1=dp[i-1][1]+dp[i-2][1]
        dp.append([temp0,temp1])
    return dp[n]

N = int(input())
for _ in range(N):
    n = int(input())
    result = fibonacci(n)
    print(result[0],result[1],sep=' ')

