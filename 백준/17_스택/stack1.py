import sys
sys.stdin=open("input.txt","rt")
class Stack:
    def __init__(self): #생성자.. 
        self.list=[]
    def push(self,X):
        self.list.append(X)
    def pop(self):
        if (len(self.list))==0:
            print(-1)
        else:
            print(self.list.pop())        
    def size(self):
        print(len(self.list))
    def empty(self):
        if (len(self.list))==0:
            print(1)
        else:
            print(0)
    def top(self):
        if (len(self.list))==0:
            print(-1)
        else:
            print(self.list[-1])
N = int(sys.stdin.readline().rstrip()) #input보다 빠르게 쓸수있는것...
stack=Stack()
for i in range(N):
    op_split=sys.stdin.readline().split()
    op=op_split[0]
    if op=="push":
        stack.push(op_split[1])
    elif op=="pop":
        stack.pop()
    elif op=="size":
        stack.size()
    elif op=="empty":
        stack.empty()
    else:
        stack.top()