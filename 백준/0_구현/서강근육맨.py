import sys
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    machines = list(map(int,sys.stdin.readline().split()))
    machines.sort()
    if len(machines)%2==0:
        hap = []
        for i in range(N//2):
            hap.append(machines[i]+machines[-(i+1)])
    else:
        hap = [machines[-1]]
        for i in range(N//2):
            hap.append(machines[i]+machines[-(i+2)])
    print(max(hap))