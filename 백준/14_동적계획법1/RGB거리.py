def RGB_street(costs):
    for i in range(1,N):#각 행
        for j in range(3):#각 행의 열
            costs[i][j]+=min(costs[i-1][:j]+costs[i-1][j+1:])
    return min(costs[-1])#마지막 행에서 최소값 리턴

import sys
sys.stdin = open("c:/Users/Administrator/Documents/Algorithm/백준/14_동적계획법1/input.txt","rt")
N = int(sys.stdin.readline())
costs = []
for _ in range(N):
    costs.append(list(map(int,sys.stdin.readline().split())))

print(RGB_street(costs))