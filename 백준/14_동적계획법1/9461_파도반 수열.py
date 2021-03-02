import sys
if __name__=="__main__":
    t = int(sys.stdin.readline())
    case = [int(sys.stdin.readline()) for _ in range(t)]

    for n in case:
        dp = [0,1,1,1,2,2,3]
        if n in [1,2,3,4,5,6]:
            print(dp[n])
            continue
        for i in range(7, n+1):
            dp.append(dp[i-1]+dp[i-5])
        print(dp[n])



















'''def function(n):
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
    print(function(n))'''