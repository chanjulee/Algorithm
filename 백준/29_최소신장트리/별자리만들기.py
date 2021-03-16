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
if __name__=="__main__":
    n = int(sys.stdin.readline()) #별의 개수
    stars = [list(map(float,sys.stdin.readline().split())) for _ in range(n)]

    edges = [] #간선비용 리스트
    for i in range(n):
        for j in range(i):
            a = stars[i]
            b = stars[j]
            cost = round(((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5, 2)
            edges.append((cost,i,j)) #비용, 별1, 별2
    edges.sort() #비용순 정렬
    #print(edges)
    
    parent = [0] * (n+1)
    for i in range(1,n+1):
        parent[i] = i #부모를 자기자신으로 초기화

    result = 0
    for edge in edges: #간선확인하며 최소신장트리 만들기
        cost, a, b = edge
        if find_parent(parent,a)!=find_parent(parent,b):
            union_parent(parent,a,b)
            result += cost

    print(result)