import sys
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    Coords = []
    for _ in range(N):
        temp = list(map(int,sys.stdin.readline().split()))
        Coords.append(temp)
    Coords.sort(key=lambda x: (x[0],x[1]))
    for c in Coords:
        print(c[0],c[1])