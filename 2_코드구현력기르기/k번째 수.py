#import sys
#sys.stdin = open("c:/Users/Administrator/Documents/Algorithm/0_테스트/input.txt","rt")

def function(s, e, k, numbers):
    numbers = numbers[s-1:e]
    numbers.sort()
    return numbers[k-1]    

T = int(input())
for t in range(T):
    n,s,e,k = map(int, input().split())
    numbers = list(map(int,input().split()))
    print("#%d %d" %(t+1, function(s, e, k, numbers)))