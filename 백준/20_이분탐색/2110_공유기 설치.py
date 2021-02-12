import sys
if __name__=="__main__":
    N, C = map(int,sys.stdin.readline().split())
    houses = [int(sys.stdin.readline()) for _ in range(N)]
    houses.sort()

    #구해야하는 것! 공유기 사이의 거리
    start = 0
    end = houses[-1]-houses[0]
    result = 0 #공유기 사이의 최대거리

    while start<=end:
        mid = (start+end)//2
        temp = houses[0]
        count = 1
        for x in houses[1:]:
            if x-temp>=mid:
                count += 1
                temp = x
        if count<C:
            end = mid-1
        else:
            result = mid
            start = mid+1            
    
    print(result)
