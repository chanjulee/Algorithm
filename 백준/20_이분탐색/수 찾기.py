def binary_search(array, target, start, end):
    if start>end: return 0
    mid = (start+end)//2
    if array[mid]==target:
        return 1
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

import sys
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    dataN = list(map(int,sys.stdin.readline().split()))
    dataN.sort()
    M = int(sys.stdin.readline())
    dataM = list(map(int,sys.stdin.readline().split()))    
    for d in dataM:
        print(binary_search(dataN, d, 0, len(dataN)-1))

'''
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
'''