def func(n):
    return n+sum(map(int,str(n)))

numList = []
for x in range(1,10001):
    numList.append(func(x))
for y in range(1,10001):
    if y not in numList:print(y)