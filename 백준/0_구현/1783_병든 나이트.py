import sys
if __name__ == "__main__":
    N, M = map(int,sys.stdin.readline().split())
    
    if N>=3 and M>=7: #이동 방법을 모두 사용하는 경우.
        print(M-2)
    elif N>=3 and M<7: #가로가 충분하지 않음. 1번,4번 번갈아 가는 방법.
        print(min(4,M))
    else: #세로가 충분하지 않음. 2번,3번 번갈아 가거나 이동 불가.
        if N==2:
            print(min(4,1+(M-1)//2))
        else:
            print(1)

'''
2 11 > 4
3 7 > 5
2 5 > 3
'''