import sys
if __name__ == "__main__":
    N,M = map(int,sys.stdin.readline().split())
    NM = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
    #print(NM)
    result = 1
    for i in range(N):
        for j in range(M):
            dot = NM[i][j]
            resultTemp = 1
            for x in range(1,50):
                if i+x>N-1 or j+x>M-1: break
                if dot==NM[i][j+x] and NM[i][j+x]==NM[i+x][j+x] and NM[i+x][j+x]==NM[i+x][j]:
                    resultTemp = (x+1)*(x+1)
            result = max(result,resultTemp)
    print(result)