def groupWord(x):
    arr = [x[0]]
    temp = arr[0]
    for a in x[1:]:
        if a==temp:
            continue
        else:
            if a in arr:
                return 0
            else:
                arr.append(a)
                temp = a
    return 1

import sys
if __name__=="__main__":
    N = int(sys.stdin.readline())
    arr = [str(sys.stdin.readline()) for _ in range(N)]
    count = 0
    for x in arr:
        count += groupWord(x)
    print(count)