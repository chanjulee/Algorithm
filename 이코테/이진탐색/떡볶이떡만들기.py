#Parametric Search
#최적화 문제를 결정 문제(예/아니오)로 바꾸어 해결하는 기법
#특정한 조건을 만족하는 가장 알맞는 값을 빠르게 찾는 최적화 문제

N, M = list(map(int,input().split())) #떡의 개수(N), 요청한 떡의 길이(M)
array = list(map(int,input().split())) #각 떡의 높이

#이진탐색을 위한 시작점과 끝점
start = 0
end = max(array)

#이진탐색 수행(반복적)
result = 0
while(start<=end):
    total = 0
    mid = (start+end)//2
    for x in array:
        #잘랐을때 떡볶이 양 계산
        if x>mid:
            total += x-mid
    #떡볶이 양이 부족:더많이자르기
    if total<M:
        end = mid-1
    #떡볶이 양이 충분:덜자르기
    else:
        result = mid #최대한 덜잘랐을 경우, 일단 기록
        start = mid+1

print(result)