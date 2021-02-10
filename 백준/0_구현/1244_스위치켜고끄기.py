def switch(status):
    if status==0: return 1
    else: return 0

def funcBoy(switches, x):
    for i in range(x-1,len(switches)):
        if (i+1)%x==0:
            switches[i] = switch(switches[i])

def funcGirl(switches, x):
    switches[x-1] = switch(switches[x-1])    
    if x==1 or x==len(switches): 
        return
    for i in range(1,min(x,len(switches)-x+1)):
        if switches[x-1-i]==switches[x-1+i]:
            switches[x-1-i] = switch(switches[x-1-i])
            switches[x-1+i] = switch(switches[x-1+i])
        else:
            return

import sys
if __name__ == "__main__":
    N = int(sys.stdin.readline()) #스위치 갯수
    switches = list(map(int,sys.stdin.readline().split())) #스위치 상태
    M = int(sys.stdin.readline()) #학생 수
    students = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
    for s in students:
        if s[0]==1: funcBoy(switches,s[1])
        else: funcGirl(switches,s[1])
    for i in range(len(switches)):
        if i!=0 and i%20==0:
            print()
        print(switches[i],end=' ')