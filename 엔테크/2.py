def solution(drum):
    n = len(drum[0])
    answer = 0

    for j in range(n):
        i = 0
        count = 0
        temp = drum[i][j]
        while True:
            if temp=='#':
                if i==n-1:
                    answer += 1
                    break
                i += 1
            elif temp=='>':
                j += 1
            elif temp=='<':
                j -= 1
            else:
                if count==1:
                    break
                else:
                    i += 1
                    count = 1
            temp = drum[i][j]

    return answer