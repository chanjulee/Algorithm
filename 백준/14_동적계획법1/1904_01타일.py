import sys
if __name__=="__main__":
    n = int(sys.stdin.readline())
    if n==1 or n==2:
        print(n)
        sys.exit()
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1]+dp[i-2])%15746
    print(dp[n])


'''def function(n):
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
print(function(N))'''