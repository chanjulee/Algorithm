'''
조건문 if(분기, 중첩)

x=15
if x>=10:
    if x%2==1:
        print("10이상의 홀수")

x=7 #중첩if
if x>0: #관계연산자
    if x<10:
        print("10보다 작은 자연수")
if x>0 and x<10: #관계연산자
    print("10보다 작은 자연수")
if 0<x<10:
    print("10보다 작은 자연수")

'''
x=10 #분기문
if x>0:
    print("양수")
else:
    print("음수")

x=93 #다중if #각자if로 하면 다 출력되어버림
if x>=90:
    print('A')
elif x>=80:
    print('B')
elif x>=70:
    print('C')
else:
    print("F")