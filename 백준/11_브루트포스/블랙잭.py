import sys
from itertools import combinations

if __name__ == "__main__":
    N, M = map(int,sys.stdin.readline().split())
    cards = list(map(int,sys.stdin.readline().split()))
    combs = []
    for c in list(combinations(cards,3)):
        temp = sum(c)
        combs.append(temp)

    combs.sort()
    for i in range(len(combs)):
        if combs[i]==M:
            print(combs[i])
            break
        elif combs[i]>M:
            print(combs[i-1])
            break
        if i==len(combs)-1: #다돌았는데도 위에 충족 안한경우...
            print(combs[i])

'''
import sys
sys.stdin=open("input.txt","rt")
N, M = map(int,sys.stdin.readline().split())
#print(condition)
cards = list(sys.stdin.readline().split())
cards.sort()
#print(cards)
answer = 0

for i in range(0, N):
    for j in range(1, N):
        for k in range(2, N):
            result = int(cards[i])+int(cards[j])+int(cards[k])
            if result <= M and result > answer:
                answer = result

print(answer)
'''