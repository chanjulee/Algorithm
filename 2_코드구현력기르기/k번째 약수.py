n, k = map(int, input().split())

'''
count = 0
temp = 0
for x in range(1,n+1):
    if n%x==0: count+=1
    if count==k:
        temp=x
        break
if temp==0: print(-1)
else: print(temp)
'''

#for else 구문
count = 0
for x in range(1,n+1):
    if n%x==0: count+=1
    if count==k:
        print(x)
        break
else: print(-1)
        