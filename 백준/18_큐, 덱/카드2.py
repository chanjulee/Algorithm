import sys
from collections import deque

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    cards = deque(range(1,N+1))
    while len(cards)>=2:
        cards.popleft()
        cards.rotate(-1)
    print(cards[0])