'''
반복문을 이용한 문제풀이
1)1부터 N까지 홀수 출력하기
2)1부터 N까지 합 구하기
3)N의 약수 출력하기
'''
n = int(input("숫자N을 입력하시오:"))#string -> int

print("======1부터N까지 홀수출력======")
for i in range(1,n+1):#1부터N까지 도는거
    if i%2==1: print(i, end=' ')

print("======1부터 N까지 합 구하기======")
sum = 0
for i in range(1,n+1):#1부터N까지 도는거
    sum += i
print(sum)

print("======N의 약수 출력하기======")
for i in range(1,n+1):#1부터N까지 도는거
    if n%i==0: print(i, end=' ')