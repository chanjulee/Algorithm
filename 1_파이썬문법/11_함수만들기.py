'''
함수 만들기
계속 반복해서 쓸 기능이 있을 때

#함수는 무조건 메인스크립트 위에~ 
#인터프리터가 이함수가 있다는것 인지
def add(a,b):
    c=a+b
    print(c)

add(3,2)
add(5,7)

def add(a,b):
    c=a+b
    return c

print(add(3,2))

def add(a,b):
    c=a+b
    d=a-b
    return c,d #정수값 두개 리턴 가능. 튜플로

print(add(3,2))
'''

def isPrime(x): #소수인지 판단
    for i in range(2,x): #소수. 1과 자기자신빼고 약수없음.
        if x%i==0: return False
    return True

a=[12,13,7,9,19]
for x in a:
    if isPrime(x): #isPrime이 참이면
        print(x,end=' ')