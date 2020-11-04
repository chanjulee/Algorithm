import sys
sys.stdin=open("input.txt","rt")
N = int(sys.stdin.readline())
print(N)

stack=[]
for i in range(N):
    num = int(sys.stdin.readline().rstrip()) #줄바꿈문자지워줌
    print(num)
    if(num==0):
        stack.pop()
    else:
        stack.append(num)
#print(sum(stack))