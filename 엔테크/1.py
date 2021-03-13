def solution(x, y):
    visited = [[0]*y for _ in range(x)]

    a = 0
    b = 0
    while True:
        if visited[a][b] == 1: #이미 방문한 곳. while문 종료.
            break
        else:
            visited[a][b] = 1
        na = a+1
        nb = b+1
        if na>x-1 or nb>y-1:
            na %= x
            nb %= y
        a = na
        b = nb

    for v in visited:
        if 0 in v:
            return False
    return True