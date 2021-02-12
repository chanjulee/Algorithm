# 분할정복(Divide&Conquer): 큰문제를 작은문제로 분할해 재귀적으로 해결

countW = 0 #White '0'
countB = 0 #Blue '1'

def colorCheck(x, y, n): #정사각형 탐색
    temp = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if temp != graph[i][j]:
                return False
    return True

def quadTree(x, y, n):
    global countW, countB
    if colorCheck(x, y, n): #탐색결과 모두 같음
        if graph[x][y]==0:
            countW += 1
        else:
            countB += 1
    else: #탐색결과 다른거 있음 >> 4등분하자
        temp = n//2
        quadTree(x, y, temp)
        quadTree(x, y+temp, temp)
        quadTree(x+temp, y, temp)
        quadTree(x+temp, y+temp, temp)

import sys
if __name__=="__main__":
    n = int(sys.stdin.readline())
    graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    quadTree(0,0,n)
    print(countW)
    print(countB)








'''import sys
sys.stdin = open("c:/Users/Administrator/Documents/Algorithm/백준/19_분할 정복/input.txt","rt")
N = int(sys.stdin.readline())
colorPaper = []
for i in range(N):
    colorPaper.append(list(map(int,sys.stdin.readline().split())))

def function(x,y,N):
    #타일 1개에 도달한 경우
    #타일 값이 0이면 [1,0], 값이 1이면 [0,1]을 리턴
    if N==1:
        return [0,1] 
    
    left_up = function(x,y,N//2)
    right_up = function(x,y+N//2,N//2)
    left_down = function(x+N//2,y,N//2)
    right_down = function(x+N//2,y+N//2,N//2)

    #사분면 네개가 전부 동일한 값일 경우 네개가 아니라 한개로 취급
    if left_up==right_up==left_down==right_down==[0,1] or left_up==right_up==left_down==right_down==[1,0]:
        return left_up
    else:
        #사분면 네개의 리스트 값을 idx별로 합한 결과를 리턴
        return list(map(sum,zip(left_up,right_up,right_down,left_down)))

white,blue = 0,0
function(0,0,N)
print(white)
print(blue)'''