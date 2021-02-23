import sys
if __name__=="__main__":
    n = int(sys.stdin.readline())
    strg = list(map(int,sys.stdin.readline().split()))
    
    dp = [0] * n
    dp[0] = strg[0]
    dp[1] = max(dp[0], strg[1])
    for i in range(2, n): #Bottom-Up
        dp[i] = max(dp[i-1], dp[i-2]+strg[i])

    print(dp[-1])