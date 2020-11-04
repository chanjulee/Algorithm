import sys
sys.stdin=open("input.txt","rt")
N = list(sys.stdin.read().split('.\n'))
N.pop()
print(N)

for i in N:
    M = list(i)
    #print(M)
    stack=[]
    for j in M:
        if j == "(":
            stack.append(j)
        elif j == ")":
            if len(stack)==0:
                stack.append(j)
                break
            elif stack[len(stack)-1]!="(":
                stack.append(j)
                break
            else:
                stack.pop()
        elif j == "[":
            stack.append(j)
        elif j == "]":
            if len(stack)==0:
                stack.append(j)
                break
            elif stack[len(stack)-1]!="[":
                break
            else:
                stack.pop()
    # print(stackA)    
    # print(stackB)
    if len(stack)==0:
        print("yes")
    else:
        print("no")


