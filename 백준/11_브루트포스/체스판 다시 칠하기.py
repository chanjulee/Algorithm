def countWB(tempChess):
    cnt1 = 0 #처음칸 W
    for i in range(8):
        for j in range(8):
            if i%2==0 and j%2==0: #W여야함
                if tempChess[i][j]!='W':
                    cnt1 += 1
            elif i%2==1 and j%2==1: #W여야함
                if tempChess[i][j]!='W':
                    cnt1 += 1
            else: #B여야함
                if tempChess[i][j]!='B':
                    cnt1 += 1
    cnt2 = 0 #처음칸 B
    for i in range(8):
        for j in range(8):
            if i%2==0 and j%2==0: #B여야함
                if tempChess[i][j]!='B':
                    cnt2 += 1
            elif i%2==1 and j%2==1: #B여야함
                if tempChess[i][j]!='B':
                    cnt2 += 1
            else: #W여야함
                if tempChess[i][j]!='W':
                    cnt2 += 1
    #print("cnt1:", cnt1, ",cnt2:", cnt2)
    return min(cnt1,cnt2)

import sys
if __name__ == "__main__":
    N, M = map(int,sys.stdin.readline().split())
    Chess = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
    count = []
    for i in range(N-7):
        for j in range(M-7):
            tempChess = [temp[j:(8+j)] for temp in Chess[i:(8+i)]] #참고
            count.append(countWB(tempChess))
    print(min(count))