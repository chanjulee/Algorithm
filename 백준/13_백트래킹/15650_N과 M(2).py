import sys
def backtracking(s,L): #(시작,길이)
    if L==M: #길이조건 만족
        #print(*result)
        for x in result:
            print(x,end=' ')
        print()
        #print("if")
    else:
        for i in range(s,N+1):
            result[L] = i
            backtracking(i+1,L+1) #오름차순
            #print("else")

if __name__=="__main__":
    N, M = map(int,sys.stdin.readline().split())
    result = [0]*M
    backtracking(1,0)
