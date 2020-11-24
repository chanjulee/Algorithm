def function(n):
    dp = [None,1,2]
    if n==1:
        return 1
    elif n==2:
        return 2
    for i in range(3,n+1):
        temp=(dp[i-1]+dp[i-2])%15746
        dp.append(temp)
    return dp[n]

N = int(input())
print(function(N))