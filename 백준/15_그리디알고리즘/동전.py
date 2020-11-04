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

# for i in coins:
#     while i<=K and K!=0:
#         K-=i
#         result+=1
#     if K==0:
#         break
# print(result)