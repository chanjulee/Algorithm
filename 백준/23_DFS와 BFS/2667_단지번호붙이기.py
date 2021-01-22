import sys
count = 0
#from collections import deque

# def bfs(x,y):
#     queue = deque([houses[x][y]])
#     while queue:
#         temp = queue.popleft()
        
def dfs(x,y):
    global count #전역변수 count를 사용하겠다
    if x<0 or x>=N or y<0 or y>=N:
        return False
    if houses[x][y] == '1':
        count += 1
        houses[x][y] = '0'
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    houses = [list(sys.stdin.readline()) for _ in range(N)]
    complexes = []
    for i in range(N):
        for j in range(N):
            count = 0
            if dfs(i,j):
                complexes.append(count)
    complexes.sort()
    print(len(complexes))
    for x in complexes: print(x)