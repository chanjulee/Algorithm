def solution(nums):
    numsSet = set(nums)
    if len(nums)/2 >= len(numsSet): 
        return len(numsSet)
    elif len(nums)/2 < len(numsSet): 
        return len(nums)/2

nums = [3,1,2,3]
print(solution(nums))