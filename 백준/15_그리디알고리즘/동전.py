import sys
if __name__ == "__main__":
    N, K = map(int,sys.stdin.readline().split())
    data = [int(sys.stdin.readline()) for _ in range(N)]
    data.sort(reverse=True)
    count = 0
    for X in data:
        if X>K: continue
        count += K//X
        K %= X
    print(count)

'''
import sys
sys.stdin=open("input.txt","rt")
N, K = map(int,sys.stdin.readline().split())

coins = []
count = 0
for i in range(N):
    coin = int(sys.stdin.readline().rstrip())
    coins.append(coin)
coins.sort(reverse=True)

for i in coins:
    if i>K:
        continue
    else:
        split = K//i
        K -= split*i
        count += split
print(count)
'''