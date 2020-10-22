'''
람다 함수
익명의 함수
람다 표현식

def plusOne(x):
    return x+1
print(plusOne(1))

plusTwo = lambda x: x+2 #변수plusTwo에 할당
print(plusTwo(1))
'''
#내장함수의 인자로 사용하면 편리
def plusOne(x):
    return x+1

a=[1,2,3]
print(list(map(plusOne, a)))#map(함수명, 자료들) map(int, list())
print(list(map(lambda x: x+1, a)))

#sort의 인자로 lambda쓰는 경우