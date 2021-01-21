import sys 
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    invited = [False] * (n+1)
    relation = [[] for _ in range(n+1)]
    for _ in range(m):
        i, j = map(int,sys.stdin.readline().split())
        relation[i].append(j)
        relation[j].append(i)
    for i in relation[1]:
        invited[i] = True
        for j in relation[i]:
            invited[j] = True
    print(invited.count(True)-1)