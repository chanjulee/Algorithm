def solution(nums):
    numsSet = set(nums)
    if len(nums)/2 >= len(numsSet): 
        return len(numsSet)
    else: 
        return int(len(nums)/2)