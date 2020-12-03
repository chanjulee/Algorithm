def lis_bitonic_function(nums):
    dpR = [1]*N
    for i in range(1,N):
        for j in range(i):
            if nums[i]>nums[j]:
                dpR[i] = max(dpR[i],dpR[j]+1)
    
    dpL = [1]*N
    nums.reverse()
    for i in range(1,N):
        for j in range(i):
            if nums[i]>nums[j]:
                dpL[i] = max(dpL[i],dpL[j]+1)
    dpL.reverse()

    dpS = [0]*N
    for i in range(N):
        dpS[i] = dpR[i]+dpL[i]-1
    
    return max(dpS)

import sys
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
print(lis_bitonic_function(nums))