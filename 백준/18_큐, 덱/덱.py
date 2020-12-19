import sys
from collections import deque

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    queue = deque() #빈 큐 만들기
    for _ in range(N):
        S = list(sys.stdin.readline().split())
        if S[0] == 'push_front':
            queue.appendleft(S[1])
        elif S[0] == 'push_back':
            queue.append(S[1])
        elif S[0] == 'pop_front':
            if len(queue) == 0: print(-1)
            else: print(queue.popleft())
        elif S[0] == 'pop_back':
            if len(queue) == 0: print(-1)
            else: print(queue.pop())
        elif S[0] == 'size':
            print(len(queue))
        elif S[0] == 'empty':
            if len(queue) == 0: print(1)
            else: print(0)        
        elif S[0] == 'front':
            if len(queue) == 0: print(-1)
            else: print(queue[0])
        elif S[0] == 'back':
            if len(queue) == 0: print(-1)
            else: print(queue[-1])
        else:
            print('error')