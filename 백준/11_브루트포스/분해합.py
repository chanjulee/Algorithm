import sys
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    answer = 0
    for n in range(1,N):
        if n+sum(map(int,str(n)))==N:
            answer = n
            break
    print(answer)
    






















'''
N = 216
answer = 0
for i in range(1,N):
    if i+sum(map(int,str(i))) == N:
        answer = i
        break

print(answer)
'''