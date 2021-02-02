import sys
def backtracking(L):
    if L==M: #길이조건 만족
        for x in result:
            print(x,end=' ')
        print()
    else:
        for i in range(1,N+1):
            result[L] = i
            backtracking(L+1)

if __name__=="__main__":
    N, M = map(int,sys.stdin.readline().split())
    result = [0]*M
    backtracking(0)