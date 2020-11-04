import sys
sys.stdin = open("input.txt","rt")
expression = list(map(str,sys.stdin.readline().split('-')))

bracket = []
for i in expression:
    temp = sum(map(int,i.split('+')))
    bracket.append(temp)

result = bracket[0]
for i in range(1,len(bracket),1):
    result -= bracket[i]

print(result)