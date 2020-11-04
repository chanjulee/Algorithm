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