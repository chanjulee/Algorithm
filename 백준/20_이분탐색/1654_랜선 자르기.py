import sys
if __name__=="__main__":
    K, N = map(int,sys.stdin.readline().split())
    lines = [int(sys.stdin.readline()) for _ in range(K)]

    start = 0 #ZeroDivisionError start=1하기...
    end = max(lines)

    result = 0
    while start<=end:
        count = 0
        mid = (start+end)//2 #1 1 \n 1 했더니 ZeroDivisionError
        if mid<1: 
            mid=1        
        for x in lines:
            if x>=mid:
                count += x//mid
        if count<N: #갯수부족:짧게자르기
            end = mid-1
        else: #갯수충분:크게자르기
            result = mid
            start = mid+1
    
    print(result)






'''import sys
def cutLAN(target,data):
    #이진 탐색을 위한 시작점과 끝점
    start = 0
    end = data[-1]

    #이진 탐색 수행(반복적)
    result = 0
    while start<=end:
        total = 0
        mid = (start+end)//2
        #1 1 \n 1 했더니 ZeroDivisionError
        if end==1:
            mid = 1
        #잘랐을 때 갯수 계산
        for x in data:            
            if x>= mid: total += x//mid
        #갯수가 부족해! >> mid 줄여
        if total<target:
            end = mid-1
        #갯수가 충족함! >> mid 늘려봐
        else:
            result = mid #최대한 덜 잘랐을 때가 정답이니, 여기서 일단 저장.
            start = mid+1
    
    return result

if __name__ == "__main__":
    N, M = map(int,sys.stdin.readline().split())
    lines = [int(sys.stdin.readline()) for _ in range(N)]
    lines.sort()
    print(cutLAN(M, lines))'''