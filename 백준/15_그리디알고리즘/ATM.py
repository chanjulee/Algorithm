import sys
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    data = list(map(int,sys.stdin.readline().split()))
    data.sort(reverse=True)

    result = 0
    for i in range(N):
        result += data[i]*(i+1)
    
    print(result)

'''import sys
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
print(sum)'''