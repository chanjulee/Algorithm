import sys
if __name__ == "__main__":
    expression = list(map(str,sys.stdin.readline().split('-')))

    if '+' in expression[0]:
        result = sum(list(map(int,expression[0].split('+'))))
    else:
        result = int(expression[0])

    for x in expression[1:]:
        result -= sum(list(map(int,x.split('+'))))

    print(result)

'''
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
'''