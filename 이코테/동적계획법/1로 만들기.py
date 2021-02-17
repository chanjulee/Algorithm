'''def makeOne(x):
    if x==1:
        return
탑다운인가? 했으나...
'''
import sys
if __name__=="__main__":
    x = int(sys.stdin.readline())
    dp = [0] * (x+1)
    dp[1] = 0 #바닥조건. bottom-up
    for i in range(2, x+1):
        temp = [dp[i-1]]
        if i%5==0:
            temp.append(dp[i//5])
        if i%3==0:
            temp.append(dp[i//3])
        if i%2==0:
            temp.append(dp[i//2])
        dp[i] = min(temp)+1
    print(dp[x])

