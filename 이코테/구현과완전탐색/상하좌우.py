import sys
n = int(sys.stdin.readline())
arr = list(sys.stdin.readline().split())

#L R U D
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def function(x,y,p):
    nx = x + dx[p]
    ny = y + dy[p]
    if nx<1 or ny<1 or nx>n or ny>n:
        return x, y
    return nx, ny

x = 1
y = 1
for a in arr:
    if a=='L':
        x, y = function(x,y,0)
    elif a=='R':
        x, y = function(x,y,1)
    elif a=='U':
        x, y = function(x,y,2)
    else:
        x, y = function(x,y,3)

print(x, y)