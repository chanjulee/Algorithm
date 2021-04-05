import sys
import itertools
if __name__=="__main__":
    n, m = map(int,sys.stdin.readline().split())
    graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    
    arrTwo = [] #치킨집 위치
    arrOne = [] #집 위치
    for i in range(n):
        for j in range(n):
            if graph[i][j]==2:
                arrTwo.append((i,j))
            if graph[i][j]==1:
                arrOne.append((i,j))

    cost = [] #거리 저장
    for one in arrOne:
        x = one[0]
        y = one[1]
        temp = []
        for two in arrTwo:
            a = two[0]
            b = two[1]
            temp2 = abs(x-a)+abs(y-b)
            temp.append(temp2)
        cost.append(temp)

    result = 0
    if len(arrTwo)==m:        
        for c in cost:
            result += min(c)
        print(result)
        sys.exit()
    
    result = 1e9
    #치킨집을 m개 고르는 경우의 수
    case = list(itertools.combinations(list(range(0,len(arrTwo))),m))
    for c in case:
        temp = [200]*len(arrOne)
        for i in c:
            for j in range(len(arrOne)):
                temp[j] = min(temp[j], cost[j][i])
        result = min(result, sum(temp))

    print(result)