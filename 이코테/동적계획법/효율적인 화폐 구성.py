import sys
if __name__=="__main__":
    n, m = map(int,sys.stdin.readline().split())
    coin = [int(sys.stdin.readline()) for _ in range(n)]

    dp = [-1] * (m+1)
    for c in coin:
        if c>m:
            continue
        dp[c] = 1
    for i in range(coin[0]+1, m+1):
        temp = []
        for c in coin:
            if dp[i-c]!=-1:
                temp.append(dp[i-c])
        if len(temp)!=0:
            dp[i] = min(temp)+1

    print(dp[m])
