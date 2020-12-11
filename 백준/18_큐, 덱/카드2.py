import sys
from collections import deque

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    cards = deque()
    for c in range(1,N+1):
        cards.append(c)
    while len(cards)>=2:
        cards.popleft()
        temp = cards.popleft()
        cards.append(temp)
    print(cards[0])