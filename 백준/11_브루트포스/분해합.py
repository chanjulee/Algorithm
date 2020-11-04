N = 216
answer = 0
for i in range(1,N):
    if i+sum(map(int,str(i))) == N:
        answer = i
        break

print(answer)