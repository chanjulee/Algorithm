def solution(board):
    answer = 0
    dx = [-1,0,1,0] #상,우,하,좌
    dy = [0,1,0,-1]
    ex = [-2,0,2,0]
    ey = [0,2,0,-2]
    for i in range(8):
        for j in range(8):
            if board[i][j]==1: #검은돌 발견
                tempCount = 0
                for k in range(4): #인접한흰돌 뒤집을수있는지
                    wi = i+dx[k]
                    wj = j+dy[k]
                    bi = i+ex[k]
                    bj = j+ex[k]
                    if wi<0 or wj<0 or bi<0 or bj<0 or wi>7 or wj>7 or bi>7 or bj>7:
                        continue
                    if board[wi][wj]==2 and board[bi][bj]==1:
                        tempCount += 1
                answer = max(answer,tempCount)
    return answer

'''
def solution(board):
    answer = 0
    dx = [-1,0,1,0] #상,우,하,좌
    dy = [0,1,0,-1]
    ex = [-2,0,2,0]
    ey = [0,2,0,-2]
    for i in range(8):
        for j in range(8):
            if board[i][j]==1: #검은돌 발견
                tempCount = 0
                for k in range(4): #인접한흰돌 뒤집을수있는지
                    wi = i+dx[k]
                    wj = j+dy[k]
                    bi = i+ex[k]
                    bj = j+ex[k]
                    if wi<0 or wj<0 or bi<0 or bj<0 or wi>7 or wj>7 or bi>7 or bj>7:
                        continue
                    if board[wi][wj]==2 and board[bi][bj]==1:
                        tempCount += 1
                answer = max(answer,tempCount)
    return answer
'''