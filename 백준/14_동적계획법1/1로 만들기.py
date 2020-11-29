def makeone(N):
    dp = [None,0,1,1]
    for x in range(4,N+1):
        if x%2==0 and x%3==0:
            temp = min(dp[x//2],dp[x//3],dp[x-1])+1
            dp.append(temp)
        elif x%2==0:
            temp = min(dp[x//2],dp[x-1])+1
            dp.append(temp)
        elif x%3==0:
            temp = min(dp[x//3],dp[x-1])+1
            dp.append(temp)
        else:
            temp = dp[x-1]+1
            dp.append(temp)         
    print(dp)
    return dp[N]

N = int(input())
print(makeone(N))