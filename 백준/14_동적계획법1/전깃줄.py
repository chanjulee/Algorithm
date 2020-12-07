import sys
def function(N, lines):
    dp = [[] for _ in range(N)] #2차원리스트. 수열저장.
    dp[0] = [lines[0][1]] #dp 바닥조건
    
    for i in range(1,N):
        temp = []
        for j in range(i):
            if lines[i][1]>dp[j][-1]: #B에 연결된 위치가 더 뒤일 때
                temp.append(dp[j])
        if len(temp)>0:
            dp[i] = max(temp, key=len) + [lines[i][1]]
        else:
            dp[i] = [lines[i][1]]          
    print(dp)
    return N-len(max(dp, key=len))

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    lines = []
    for _ in range(N):
        A,B = map(int,sys.stdin.readline().split())
        lines.append([A,B])
    lines.sort(key=lambda x: x[0]) #A오름차순 정렬
    print(function(N, lines))
