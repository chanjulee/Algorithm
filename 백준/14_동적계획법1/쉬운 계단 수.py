def easyStairs(N):
    dp = [1,1,1,1,1,1,1,1,1,1]
    for _ in range(1,N):
        temp = dp[:]
        for i in range(0,10):
            if i==0:
                dp[i]=temp[1] % 1000000000
            elif i==9:
                dp[i]=temp[8] % 1000000000
            else:
                dp[i]=temp[i-1]+temp[i+1] % 1000000000
        print(dp)
    return sum(dp[1:]) % 1000000000

N = int(input())
print(easyStairs(N))