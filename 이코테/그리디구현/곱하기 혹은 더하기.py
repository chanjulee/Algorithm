import sys
s = sys.stdin.readline().rstrip()
result = 0
for x in s:
    x = int(x)
    if result==0 or x==0 or x==1:
        result += x
    else:
        result *= x
print(result)


























'''data = input()

#첫번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1,len(data)):
    #두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num<=1 or result<=1:
        result += num
    else:
        result *= num

print(result)'''