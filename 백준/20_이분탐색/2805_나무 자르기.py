def binary_search(array,M,start,end,result):
    if start>end:
        return result
    total = 0
    mid = (start+end)//2
    for x in trees:
        if x>mid:
            total += x-mid
        else:
            break
    if total<M:
        binary_search(array,M,start,mid-1,result)
    else:
        binary_search(array,M,mid+1,end,mid)

import sys
if __name__=="__main__":
    N, M = map(int,sys.stdin.readline().split())
    trees = list(map(int,sys.stdin.readline().split()))
    trees.sort(reverse=True) #큰순서대로

    print(binary_search(trees,M,0,trees[0],0))



'''import sys
def cutTree(target,data):
    #이진 탐색 위한 시작점과 끝점
    start = 0
    end = data[-1]

    #이진 탐색 수행
    result = 0
    while start<=end :
        total = 0
        H = (start+end)//2
        #잘랐을때 양 계산
        for x in data:            
            if x>H: total+= x-H
        #양이 부족한 경우 더많이 자르기(오른쪽 부분 탐색)
        if total<target:
            end = H-1
        #양이 충분한 경우 덜 자르기(왼쪽 부분 탐색)
        else:
            result = H #최대한 덜 잘랐을 때가 정답, result
            start = H+1
    
    return result

if __name__ == "__main__":
    N, M = map(int,sys.stdin.readline().split())
    trees = list(map(int,sys.stdin.readline().split()))
    trees.sort()
    print(cutTree(M,trees))'''
    