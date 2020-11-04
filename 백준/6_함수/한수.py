def func(n):
    numList = list(map(int,str(n)))
    if len(numList)<=2: return True
    for i in range(1,len(numList)-1):
        if numList[i]-numList[i-1]!=numList[i+1]-numList[i]: return False
    return True

N = int(input())
answer = 0
for x in range(1,N+1):
    if func(x):answer+=1
print(answer)