#Union-find
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

import sys
import math
if __name__=="__main__":
    n, m = map(int,sys.stdin.readline().split()) #우주신수, 통로개수
    gods = [0] + [list(map(int,sys.stdin.readline().split())) for _ in range(n)] #우주신좌표

    edges = [] #간선비용 리스트
    for i in range(1,n):
        for j in range(i+1,n+1):
            a = gods[i]
            b = gods[j]
            cost = math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)            
            edges.append((cost,i,j)) #비용, 우주신1, 우주신2
    edges.sort()    

    parent = [0] * (n+1)
    for i in range(1,n+1):
        parent[i] = i

    for _ in range(m):
        a, b = map(int,sys.stdin.readline().split())
        union_parent(parent,a,b) #합집합 진행~~

    result = 0
    for edge in edges: #간선확인하며 최소신장트리 만들기
        cost, a, b = edge
        if find_parent(parent,a)!=find_parent(parent,b):
            union_parent(parent,a,b)
            result += cost
            #print(cost)
    print("%0.2f" %result)
        