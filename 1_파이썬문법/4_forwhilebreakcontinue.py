'''
반복문(for,while)

a = range(10)#0부터 순차적인 정수리스트 생성
print(list(a))
a = range(1,11)#1부터 10까지
print(list(a))

for i in range(10):
    print("hello", i)

for i in range(10,0,-1):#10부터 1씩작아지는 리스트
    print("hello", i)

i=1
while i<=10:
    print(i) 
    i+=1
i=10
while i>=1:
    print(i)
    i-=1

i=1
while True:#참거짓을 따지는 곳이기 때문에 무한반복임
    print(i)
    if i==10: break #무한반복에서 멈추게하는(특정조건에서 멈추게한다)
    i+=1
'''
for i in range(1,11):
    #어떤 조건에서는 건너뛰고싶을때
    if i%2==0: continue
    print(i)

#for else구문 
for i in range(1,11):#1부터10까지도는데
    print(i)
    if i==11:break#break로 종료되면 else로 안감
else:#정상종료시 else실행
    print(11)