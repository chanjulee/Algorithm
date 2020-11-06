import sys
sys.stdin = open("c:/Users/Administrator/Documents/Algorithm/백준/19_분할 정복/input.txt","rt")
A, B, C = map(int,sys.stdin.readline().split())

def function(A,B):
    if B==1:
        return A
    elif B%2==0:
        return function(A,B//2)**2%C
    else:
        return function(A,B-1)*A%C

print(function(A,B))