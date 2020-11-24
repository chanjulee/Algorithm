import sys
sys.stdin = open("c:/Users/Administrator/Documents/Algorithm/백준/19_분할 정복/input.txt","rt")
N = int(input())
matrix = [input() for _ in range(N)]
'''
def function(x,y,N):
    temp = matrix[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if temp!=matrix[i][j]:
                left_up = function(x,y,N//2)
                right_up = function(x,y+N//2,N//2)
                left_down = function(x+N//2,y,N//2)
                right_down = function(x+N//2,y+N//2,N//2)
                print("("+left_up+right_down+left_down+right_down+")")
                return
    if temp==0:
        print('0',end='')
        return
    else:
        print('1',end='')
        return

'''
def function(x,y,N):
    if N==1:
        return matrix[y][x]

    #4분할
    left_up = function(x,y,N//2)
    right_up = function(x,y+N//2,N//2)
    left_down = function(x+N//2,y,N//2)
    right_down = function(x+N//2,y+N//2,N//2)

    #모두 같은 값일 경우 하나만 출력
    if left_up==right_up==left_down==right_down:
        return left_up
    return "("+left_up+right_down+left_down+right_down+")"

print(function(0,0,N))