import sys
from collections import deque

def printer(files,index,target):
    count = 0 #인쇄
    while True:
        maxNum = max(files)
        if files[0]==maxNum:
            count += 1
            if index[0]==target:
                break
            files.popleft()
            index.popleft()
        else:
            files.rotate(-1)
            index.rotate(-1)
    return count

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    for _ in range(N):
        M,I = map(int,sys.stdin.readline().split())
        files = deque(map(int,sys.stdin.readline().split())) #문서중요도
        index = deque(range(0,M)) #문서위치
        print(printer(files,index,I))        