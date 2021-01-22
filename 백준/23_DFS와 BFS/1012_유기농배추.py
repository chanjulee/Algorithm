import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)

def dfs(x,y):
    if x<0 or x>=N or y<0 or y>=M:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x-1,y)
        return True
    return False

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T):
        N, M, K = map(int,sys.stdin.readline().split())
        graph = [[0]*M for _ in range(N)]
        for _ in range(K):
            x, y = map(int,sys.stdin.readline().split())
            graph[x][y] = 1
        result = 0
        for x in range(N):
            for y in range(M):
                if dfs(x,y):
                    result += 1
        print(result)
    