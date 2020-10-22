'''
문자열과 내장함수
'''
msg = "It is Time"
print(msg.upper())#msg는 그대로있고 대문자화시켜서 출력
print(msg.lower())
print(msg)

tmp = msg.upper()
print(tmp)
print(tmp.find('T'))#첫번째 T의 문자열인덱스 번호 출력
print(tmp.count('T'))#문자열에서 대문자 T갯수 출력

print(msg[:2])#0이상 2미만
print(msg[3:5])#3이상 4미만 즉, 3 4
print(len(msg))

for i in range(len(msg)):#10 즉, 0부터 9까지 돈다
    print(msg[i], end=' ')
print()

for x in msg:#배열에 모두 접근
    print(x, end=' ')
print()

for x in msg:
    if x.isupper():#x가 대문자이면 참
        print(x, end=' ')
print()

for x in msg:
    if x.islower():#x가 소문자이면 참
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha():#x가 알파벳이면 참. 공백빼고 출력됨
        print(x, end='')
print()

tmp='AZ'#A는 65 Z는 90
for x in tmp:
    print(ord(x))#ord(x) 아스키넘버출력함수

tmp='az'#a는 97 z는 122
for x in tmp:
    print(ord(x))#ord(x) 아스키넘버출력함수

tmp=66
print(chr(tmp))#chr(tmp) 아스키넘버를문자로출력