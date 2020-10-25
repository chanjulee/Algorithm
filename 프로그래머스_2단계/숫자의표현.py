def solution(num):
    answer = 1 #자기 자신
    '''
    numbers = [] #1과 자신 제외 약수리스트
    for i in range(1,n//2+1):
        if n%i==0: numbers.append(i)
    print(numbers)
            
    for x in numbers:
        y = n/x #x*y=n
        if y%2==0 : continue
        if (y-1)/2>x : continue
        answer+=1
    if n%2==1: 
        answer+=1 
        answer+=1
    '''    #등차수열의 합
    print([i  for i in range(1,n+1,2) if n % i == 0])
    return len([i  for i in range(1,n+1,2) if n % i == 0])