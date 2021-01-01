import sys
from collections import Counter
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    nums = [int(sys.stdin.readline()) for _ in range(N)]
    nums.sort() #오름차순 정렬
    count = Counter(nums).most_common() #개채별로 카운트 및 나열
    #count = sorted(c.items(),key=lambda x:(-x[]))
    #print(count)

    print(int(round(sum(nums)/N,0))) #산술평균
    print(nums[N//2]) #중앙값
    if len(count)==1: print(count[0][0])
    elif count[0][1]==count[1][1]: print(count[1][0])
    else: print(count[0][0]) #최빈값
    print(nums[-1]-nums[0]) #범위