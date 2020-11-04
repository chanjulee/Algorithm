import sys
sys.stdin=open("input.txt","rt")
N = int(sys.stdin.readline())

for i in range(N):
    num = list(sys.stdin.readline())
    for j in num:
        print(j)