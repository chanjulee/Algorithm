'''
리스트와 내장함수(1)
'''
import random as r #r로 명령하겠다

a=[] #빈 리스트 a=list()
#print(a)

a=[1,2,3,4,5]
#print(a) #print(list(a))
#print(a[0])

b=list(range(1,11))#또다른 초기화방법
#print(b)

c=a+b #두리스트를 합치는방법
#print(c)

a.append(6) #제일 뒤에 6추가 append
#[1, 2, 3, 4, 5, 6]
a.insert(3,7) #3번 인덱스에 7추가 insert
#[1, 2, 3, 7, 4, 5, 6]
a.pop() #제일 뒤에 자리 하나뺌
#[1, 2, 3, 7, 4, 5]
a.pop(3) #3번인덱스 하나뺌
#[1, 2, 3, 4, 5]
a.remove(4) #4라는 값 하나뺌
#[1, 2, 3, 5]
#print(a.index(5)) #5의 인덱스값

a=list(range(1,11))
print(a)
print(sum(a)) #list a의 합 sum
print(max(a))
print(min(a)) #list값들(인자값) 중에 최솟값.
print(min(7,3,5)) #인자들 중에 최솟값. 3

r.shuffle(a) #a를 무작위로 섞겠다. 게임만들때 씀
print(a) 
a.sort() #오름차순 정렬
print(a)
a.sort(reverse=True) #내림차순 정렬
print(a)

a.clear() #다 지워
print(a)