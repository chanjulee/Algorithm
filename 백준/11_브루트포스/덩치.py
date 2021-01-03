import sys
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    chart = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    for c in chart:
        temp = 1
        for d in chart:
            if c[0]<d[0] and c[1]<d[1]:
                temp += 1
        print(temp,end=' ')










'''
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
'''