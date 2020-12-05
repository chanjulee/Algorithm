import sys

def findNum(target, data):
    start = 0
    end = len(data)-1
    while start<=end:
        mid = (start+end)//2
        if data[mid]==target:
            return 1
        elif data[mid]<target:
            start = mid+1
        else:
            end = mid-1
    return 0

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    A = list(map(int,sys.stdin.readline().split()))
    A.sort()
    M = int(sys.stdin.readline())
    B = list(map(int,sys.stdin.readline().split()))
    for x in B:
        print(findNum(x, A))