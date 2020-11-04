import sys
sys.stdin=open("input.txt","rt")
N = int(sys.stdin.readline())
men = list(map(int,sys.stdin.readline().split()))
men.sort(reverse=True)
#print(men)

sum = 0
count = 0
for i in men:
    count+=1
    sum+=count*i
print(sum)