import sys
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
print(blue)