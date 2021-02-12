result = []

def colorCheck(x, y, n):
    temp = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j]!=temp:
                return False
    return True

def quadTree(x, y, n):
    global result
    if colorCheck(x, y, n):
        result.append(graph[x][y])
    else:
        result.append("(")
        temp = n//2
        quadTree(x, y, temp)
        quadTree(x, y+temp, temp)
        quadTree(x+temp, y, temp)
        quadTree(x+temp, y+temp, temp)
        result.append(")")

import sys
if __name__=="__main__":
    n = int(sys.stdin.readline())
    graph = [list(sys.stdin.readline()) for _ in range(n)]
    quadTree(0, 0, n)
    for x in result:
        print(x, end='')