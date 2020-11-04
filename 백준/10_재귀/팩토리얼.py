'''
N = int(input())
answer = 1
for x in range(2,N+1):
    answer *= x
print(answer)
'''
def factorial(n):
    if n==0: return 1
    else: return n*factorial(n-1)

N = int(input())
print(factorial(N))