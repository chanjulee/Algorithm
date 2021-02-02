import sys
def backtracking(s,L): #(시작,길이)
    if L==M: #길이조건 만족
        for x in result:
            print(x,end=' ')
        print()
    else:
        for i in range(s,N+1):
            result[L] = i
            backtracking(i,L+1) #비내림차순

if __name__=="__main__":
    N, M = map(int,sys.stdin.readline().split())
    result = [0]*M
    backtracking(1,0)