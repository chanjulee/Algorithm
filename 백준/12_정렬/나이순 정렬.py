import sys
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    members = []
    for i in range(N):
        x, y = sys.stdin.readline().split()
        temp = [i,int(x),y]
        members.append(temp)
    members.sort(key=lambda x:(x[1],x[0]))
    for m in members:
        print(m[1], m[2])