N = 25
K = 5
count = 0
while N!=1:
    if N%K==0 :
        N = N/K
        count += 1
    else:
        N -= 1
        count += 1
print(count)
''' 로그N 코드...
result = 0
while True:
    #N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (N//K)*K
    result += (N-target) #1을 빼는 연산횟수 한번에
    N = target #K로 나누어 떨어지는 수
    #N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if N<K:
        break
    #K로 나누는 연산
    result += 1
    N = N//k
#마지막으로 남은 수에 대하여 1씩 빼기
result += (N-1)
print(result)
'''
        
'''
주어진 N에 대하여 최대한 많이 나누기를 수행하면 됨.
N의 값을 줄일 때, 2이상의 수로 나누는 작업이 1을 빼는 작업보다
수를 훨씬 많이 줄일 수 있음.
'''