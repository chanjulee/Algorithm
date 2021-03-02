import sys
if __name__=="__main__":
    n = int(sys.stdin.readline())
    arr = [int(sys.stdin.readline()) for _ in range(n)]

    if n==1:
        print(arr[0])
        sys.exit()
    if n==2:
        print(arr[0] + arr[1])
        sys.exit()
    if n==3:
        print(max(arr[0]+arr[2], arr[1]+arr[2]))
        sys.exit()

    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0]+arr[2], arr[1]+arr[2])

    for i in range(3, n):
        temp1 = arr[i] + arr[i-1] + dp[i-3] #지금, 이전
        temp2 = arr[i] + dp[i-2] #지금, 이전전
        dp[i] = max(temp1, temp2)

    print(dp[-1])















'''def go_upstairs(N,stairs):
    dp = [0]*N
    dp[0] = stairs[0]
    if N==1: return dp[0]
    dp[1] = stairs[0]+stairs[1]
    if N==2: return dp[1]
    dp[2] = max(stairs[0],stairs[1])+stairs[2]
    if N==3: return dp[2]
    
    for i in range(3,N):
        #max(직전 계단을 밟은 경우, 직전 계단을 밟지 않은 경우)
        dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+dp[i-2])

    return dp[N-1]

N = int(input())
stairs = []
for _ in range(N):
    temp = int(input())
    stairs.append(temp)

print(go_upstairs(N,stairs))'''