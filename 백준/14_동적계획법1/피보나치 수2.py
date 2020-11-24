def fibonacci(n):
    dp = [0,1]
    for i in range(2,n+1):
        temp=dp[i-1]+dp[i-2]
        dp.append(temp)
    return dp[n]

n = int(input())
print(fibonacci(n))