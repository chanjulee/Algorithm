import sys
def backtracking(L):
    if L==M: #길이조건 만족
        for x in result:
            print(x,end=' ')
        print()
    else:
        for i in range(1,N+1):
            if not visited[i]: #방문x
                visited[i] = True #방문처리
                result[L] = i # result[0]=1
                backtracking(L+1) # result[1]=2 #result[2]=3...
                visited[i] = False

if __name__=="__main__":
    N, M = map(int,sys.stdin.readline().split())
    visited = [False]*(N+1)
    result = [0]*M
    backtracking(0)
