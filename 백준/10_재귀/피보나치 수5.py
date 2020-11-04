'''
N = int(input())
numList = [0,1]
for i in range(2,N+1):
    temp = numList[i-1]+numList[i-2]
    numList.append(temp)
print(numList[N])
'''
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n-1)+fibonacci(n-2)

N = int(input())
print(fibonacci(N))