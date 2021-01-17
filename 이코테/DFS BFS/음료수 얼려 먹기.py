def dfs(x,y):
    #종료조건: 범위 벗어났을 때
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False

    if graph[x][y]==0:
        #해당노드 방문처리
        graph[x][y] = 1
        #상하좌우 재귀호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True

    return False

if __name__ == "__main__":
    n, m = map(int,input().split())
    graph = [list(map(int,input())) for _ in range(n)]

    result = 0
    #모든 노드 돌면서 음료수 채우기
    for i in range(n):
        for j in range(m):
            #dfs 수행위치
            if dfs(i,j)==True:
                result += 1

    print(result)
