import sys
def different(teamStart,teamLink):
    sumStart = 0
    for i in teamStart:
        for j in teamStart:
            if i==j: continue
            sumStart += graph[i-1][j-1]
    sumLink = 0
    for i in teamLink:
        for j in teamLink:
            if i==j: continue
            sumLink += graph[i-1][j-1]
    differentList.append(abs(sumStart-sumLink))

def team(s,L):
    if L==N//2: #teamStart 찼을때
        for i in range(N):
            if i not in teamStart:
                teamLink.append(i)
        different(teamStart,teamLink)
        print("teamStart",teamStart)
        print("teamLink",teamLink)
        teamStart.clear()
        teamLink.clear()
    else:
        for i in range(s,N+1):
            teamStart.append(i)
            team(i+1,L+1)

if __name__=="__main__":
    N = int(sys.stdin.readline())
    graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    teamStart = []
    teamLink = []
    differentList = []
    team(1,0)
    print(min(differentList))