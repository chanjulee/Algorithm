import sys
sys.stdin=open("input.txt","rt")
N = int(sys.stdin.readline())


for i in range(N):
    M = list(sys.stdin.readline())
    stack=[]
    for j in M:
        if j == "(":
            stack.append(j)
        elif j == ")":
            if len(stack)==0:
                stack.append(j)
                break
            else:
                stack.pop()
    if len(stack)==0:
        print("YES")
    else:
        print("NO")


