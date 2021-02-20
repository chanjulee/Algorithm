def rotation(sawteeth, n, d, status):   
    #print(sawteeth)
    flagL = False
    if n>0: #왼쪽 톱니를 돌릴까?    
        if sawteeth[n][6]!=sawteeth[n-1][2] and not status[n-1]:
            flagL = True
    flagR = False
    if n<3: #오른쪽 톱니를 돌릴까?
        if sawteeth[n][2]!=sawteeth[n+1][6] and not status[n+1]:
            flagR = True

    if d==1: #시계방향 이동
        status[n] = True
        sawteeth[n] = sawteeth[n][7] + sawteeth[n][:7]
    else: #반시계방향 이동
        status[n] = True
        sawteeth[n] = sawteeth[n][1:] + sawteeth[n][0]

    if flagL:
        rotation(sawteeth, n-1, -d, status)
    if flagR:
        rotation(sawteeth, n+1, -d, status)

import sys
if __name__=="__main__":
    sawteeth = [str(sys.stdin.readline().rstrip()) for _ in range(4)]
    k = int(sys.stdin.readline())
    for _ in range(k):
        status = [False] * 4
        n, d = map(int,sys.stdin.readline().split())
        rotation(sawteeth, n-1, d, status)
    
    result = 0
    for i, x in enumerate(sawteeth):
        if x[0]=='1':
            if i==0:
                result += 1
            elif i==1:
                result += 2
            elif i==2:
                result += 4
            else:
                result += 8
    print(result)
    