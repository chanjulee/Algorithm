import sys
sys.setrecursionlimit(10**6)
from collections import deque
n = int(sys.stdin.readline()) #보드 크기
k = int(sys.stdin.readline()) 
apple = [] #사과
for _ in range(k):
    a, b = map(int,sys.stdin.readline().split())
    apple.append([a-1, b-1])
l = int(sys.stdin.readline()) 
turnTime = []; turn = {} #방향
for _ in range(l):
    x, k = sys.stdin.readline().split()
    turnTime.append(int(x))
    turn[int(x)] = k

def move(x, y, d, count, snake):
    global n, apple, turnTime, turn

    dx = [0, 1, 0, -1] #우, 하, 좌, 상
    dy = [1, 0, -1, 0] #우, 하, 좌, 상

    if count in turnTime: #뱀의 방향 전환
        #print("방향 전환")
        temp = turn[count]
        if temp == 'D': d = (d+1)%4
        else: d = (d+3)%4

    nx = x+dx[d] #뱀의 머리 이동
    ny = y+dy[d]

    if nx>=n or ny>=n or nx<0 or ny<0 or [nx,ny] in snake: #종료 조건
        #print("종료", nx, ny, snake)
        count += 1
        return count
    
    if [nx, ny] in apple: #이동한 위치에 사과가 있는 조건
        #print("사과먹음", snake)
        snake.append([nx, ny])
        apple.remove([nx, ny])
        count += 1
        #print(count)
        return move(nx, ny, d, count, snake)

    #print("사과안먹음", snake)
    snake.popleft()
    snake.append([nx, ny])
    count += 1
    #print(count)
    return move(nx, ny, d, count, snake)

if __name__=="__main__":    
    x, y, d, count = 0, 0, 0, 0
    snake = deque([[0,0]]) 

    print(move(x, y, d, count, snake))