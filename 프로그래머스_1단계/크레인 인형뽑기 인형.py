def solution(board, moves):
    answer = 0
    
    board2 = [] 
    for i in range(len(board)):
        line = []
        for j in range(len(board)):
            if board[j][i]!= 0:line.append(board[j][i])
        board2.append(line)
    print(board2)
    #[[4, 3], [2, 2, 5], [1, 5, 4, 1], [4, 3], [3, 1, 2, 1]]
    
    basket = []
    for move in moves:
        if len(board2[move-1])==0: continue
        basket.append(board2[move-1].pop(0))
    
    for i in range(len(basket)):
        if basket[i]==basket[i+1]:
            basket.pop(i)
            basket.pop(i)
        

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board,moves)