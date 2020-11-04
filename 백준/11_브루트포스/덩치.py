import sys
sys.stdin=open("input.txt","rt")
N = int(sys.stdin.readline().strip())
men = []
for i in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    men.append((weight,height))
for i in men:
    rank = 1
    for j in men:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')