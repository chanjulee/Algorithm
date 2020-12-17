import sys
from collections import deque

if __name__ == "__main__":
    N, K = map(int,sys.stdin.readline().split())
    people = deque(range(1,N+1))

    print('<', end='')
    for _ in range(N):
        for i in range(K-1):#1,2
            people.rotate(-1)
        print(people.popleft(),end='')#3번째
        if people:
            print(', ',end='')
    print('>')
 