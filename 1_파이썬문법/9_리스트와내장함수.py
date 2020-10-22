a=[23,12,36,53,19]
print(a[:3])#인덱스0부터 3전까지
print(a[1:4])#인덱스1부터 4전까지
print(len(a))

for i in range(len(a)):#len(a)=5 0부터 4까지 돈다
    print(a[i], end=' ')
print()

for x in a:#배열에 하나하나씩 접근
    print(x, end=' ')
print()

for x in a:
    if x%2==1: print(x, end=' ') #홀수만 출력해본것
print()

for x in enumerate(a): #인덱스값까지 출력하고싶을때
    print(x) #튜플 (인덱스값,원소값)

#b=(1,2,3,4,5) #튜플
#print(b[0])
#b[0]=7 불가능. 리스트와 다른점:값변경불가

for x in enumerate(a): 
    print(x[0], x[1])

for index, value in enumerate(a):
    print(index, value)

#all함수
if all(60>x for x in a): #for문 돌면서 모두 조건 비교. all 모두 참이면 참.
    print("YES")
else:
    print("NO")

#any함수
if any(11>x for x in a): #for문 돌면서 모두 조건 비교. any 한번이라도 참이면 참.
    print("YES")
else:
    print("NO")
