import sys
#LCS: 가장 긴 길이의 공통부문자열 찾기
def functionLCS(X,Y):
    I = len(X)+1
    J = len(Y)+1
    dp = [[0]*J for _ in range(I)]
    #dp[0][j] dp[i][0]값은 0
    for i in range(1,I):
        for j in range(1,J):
            if X[i-1]==Y[j-1]: #0ACAYKP 0CAPCAK
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]

if __name__ == "__main__":
    X = sys.stdin.readline().strip()
    Y = sys.stdin.readline().strip()
    print(functionLCS(X,Y))