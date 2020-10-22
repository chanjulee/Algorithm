'''
변수입력과 연산자
'''

a=input("숫자를 입력하시오:")
print(a)

a,b=input("숫자를 입력하시오:").split()#split함수 띄어쓰기를 기준으로 분리
print(a,b)
print(type(a))#string임
c=a+b#역시 string

a=int(a)
b=int(a)

a,b=map(int, input("숫자를 입력하시오:").split()) #mapping?

print(a//b) #몫
print(a%b) #나머지
print(a**b) #a의 3제곱

a=4.3
b=5
c=a+b #정수와 실수의 연산결과는 실수임
print(type(c))