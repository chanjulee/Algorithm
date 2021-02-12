# 분할정복(Divide&Conquer): 큰문제를 작은문제로 분할해 재귀적으로 해결
# 거듭제곱의 시간초과를 분할정복으로 해결
def function(a, b):
    if b==1:
        return a%C
    else:
        temp = function(a,b//2)
        if b%2==0:
            return temp * temp % C
        else:
            return temp * temp * a % C            

import sys
if __name__=="__main__":
    A, B, C = map(int, sys.stdin.readline().split())
    print(function(A,B))




'''import sys
sys.stdin = open("c:/Users/Administrator/Documents/Algorithm/백준/19_분할 정복/input.txt","rt")
A, B, C = map(int,sys.stdin.readline().split())

def function(A,B):
    if B==1:
        return A%C
    elif B%2==0:
        return function(A,B//2)**2%C
    else:
        return function(A,B-1)*A%C

print(function(A,B))'''