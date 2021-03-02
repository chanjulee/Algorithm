import sys
if __name__=="__main__":
    n = int(sys.stdin.readline())
    arr = [int(sys.stdin.readline()) for _ in range(n)]

    if n==1:
        print(arr[0])
        sys.exit()
    if n==2:
        print(arr[0]+arr[1])
        sys.exit()
    if n==3:
        print(max(arr[0]+arr[2], arr[1]+arr[2], arr[0]+arr[1]))
        sys.exit()

    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = arr[0]+arr[1]
    dp[2] = max(arr[0]+arr[2], arr[1]+arr[2], dp[1])

    for i in range(3,n):
        temp1 = arr[i] + arr[i-1] + dp[i-3] #전에도 마시고 이번에도 마시고
        temp2 = arr[i] + dp[i-2] #전에는 안마시고 이번에만 마시고
        dp[i] = max(temp1, temp2, dp[i-1]) #dp[i-1]이 더큰지도비교... #계단에선 안비교...

    print(dp[-1])











'''def drink_wine(wines):
    dp = [0]*N
    dp[0] = wines[0]
    if N==1: return dp[0]
    dp[1] = wines[0]+wines[1]
    if N==2: return dp[1]
    dp[2] = max(wines[0],wines[1])+wines[2]
    if N==3: return dp[2]

    for i in range(3,N):
        #max(전에 마신 경우, 전전에 마신 경우)
        temp = max(dp[:i-2])
        dp[i] = max(wines[i]+wines[i-1]+dp[i-3], wines[i]+temp)
    return max(dp[-1],dp[-2])

import sys
sys.stdin = open("c:/Users/Administrator/Documents/Algorithm/백준/14_동적계획법1/input.txt","rt")
N = int(input())
wines = []
for _ in range(N):
    temp = int(input())
    wines.append(temp)

print(drink_wine(wines))'''