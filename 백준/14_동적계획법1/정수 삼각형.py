def triangle_function(nums):
    for i in range(1,N):#각 행
        for j in range(i+1):
            if j==0:
                nums[i][j]+=nums[i-1][j]
                continue
            elif j==i:
                nums[i][j]+=nums[i-1][j-1]
                continue
            else:
                nums[i][j]+=max(nums[i-1][j-1],nums[i-1][j])
    return max(nums[-1])

import sys
sys.stdin = open("c:/Users/Administrator/Documents/Algorithm/백준/14_동적계획법1/input.txt","rt")
N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    nums.append(list(map(int,sys.stdin.readline().split())))

print(triangle_function(nums))